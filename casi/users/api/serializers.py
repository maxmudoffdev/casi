import secrets
from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers

from casi.users.models import User, UserRole


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=8)
    password2 = serializers.CharField(write_only=True)
    id = serializers.UUIDField(read_only=True)
    verification_method = serializers.ChoiceField(
        choices=["email", "telegram"],
        default="email",
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "verification_method",

            "password",
            "password2"
        ]


    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password": "Passwords do not match."}
            )
        return data

    def validate_password(self,value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters."
            )
        if not any(c.isupper() for c in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")

        if not any(c.isdigit() for c in value):
            raise serializers.ValidationError("Password must contain at least one digit.")

        return  value

    def create(self, validated_data):
        validated_data.pop("password2")
        validated_data.pop("verification_method")

        token = secrets.token_urlsafe(32)

        user = User.objects.create_user(
            **validated_data,
            role=UserRole.AUTHOR,
            is_active=False,
            verification_token=token,
            verification_token_expires=timezone.now() + timedelta(minutes=3)
        )
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        return value.lower().strip()


