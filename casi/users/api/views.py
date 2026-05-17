from django.utils import timezone
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from casi.users.api.serializers import RegisterSerializers, LoginSerializer
from casi.users.api.tasks import send_verification_email
from casi.users.models import User
from django.contrib.auth import authenticate


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializers = RegisterSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        verify_method = serializers.validated_data.get("verification_method","telegram")
        user = serializers.save()

        if verify_method == "telegram":
            bot_link = f"https://t.me/casi_index_bot?start={user.verification_token}"
            return Response({
                "message": "Open Telegram bot to verify.",
                "bot_link": bot_link
            }, status=status.HTTP_201_CREATED)

        else:
            # Email — Celery task
            send_verification_email.delay(user.id)
            return Response({
                "message": "Check your email for verification link.",
                "email": user.email
            }, status=status.HTTP_201_CREATED)



class VerifyView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        code = request.data.get("code")

        # 1 — Bormi?
        if not email or not code:
            return Response(
                {"error": "Email and code are required."},
                status=status.HTTP_400_BAD_REQUEST
            )


        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not user.telegram_code_expires or user.telegram_code_expires < timezone.now():
            return Response(
                {"error": "Code expired. Please try again."},
                status=status.HTTP_400_BAD_REQUEST
            )


        if user.telegram_verification_code != code:
            return Response(
                {"error": "Invalid code."},
                status=status.HTTP_400_BAD_REQUEST
            )


        user.is_active = True
        user.telegram_verified = True
        user.telegram_verification_code = None
        user.telegram_code_expires = None
        user.verification_token = None
        user.save()

        return Response({
            "message": "Verified! ✅ Now you can login."
        })

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")


        if not email or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(request=request,email=email,password=password)
        if not user:
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        if not user.is_active:

            return Response({
                "error": "Account not verified.",
                "bot_link": f"https://t.me/casi_index_bot?start={user.verification_token}"
            }, status=status.HTTP_403_FORBIDDEN)

        refresh = RefreshToken.for_user(user)

        user.last_login = timezone.now()
        user.save(update_fields=["last_login"])

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "telegram_verified": user.telegram_verified,
            }
        })








