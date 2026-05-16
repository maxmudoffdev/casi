from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from casi.common.paginator import BasePagination
from casi.reviews.api.serializers import ReviewSerailizers, ReviewAssigmentSerializer
from casi.reviews.models import Review,ReviewAssigment


class AllReviewView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        review = Review.objects.all()
        paginator = BasePagination()
        page = paginator.paginate_queryset(queryset=review,request=request)
        serialziers = ReviewSerailizers(page,many=True,context={"request": request})
        return paginator.get_paginated_response(serialziers.data)

    def post(self,request):
        serialziers = ReviewSerailizers(data=request.data,context={"request": request})
        serialziers.is_valid(raise_exception=True)
        serialziers.save()
        return Response({
            "message":"Review created",
            "data":serialziers.data
        },
            status=status.HTTP_201_CREATED
        )


class ReviewDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,id):
        review = get_object_or_404(Review,id=id)
        serailizers = ReviewSerailizers(review,context={"request":request})
        return Response(
            serailizers.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, id):
        review = get_object_or_404(Review,id=id)
        if review.is_submitted:
            return Response(
                {"error": "Submitted review cannot be edited."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serailizers = ReviewSerailizers(review,data=request.data,partial=True, context={"request": request})
        serailizers.is_valid(raise_exception=True)
        serailizers.save()
        return Response(
            {
                "message":"Review is updated",
                "data":serailizers.data
            },
            status=status.HTTP_200_OK
        )

    def delete(self, request, id):
        review = get_object_or_404(Review,id=id)
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class SubmitView(APIView):
    permission_classes = [AllowAny]
    def post(self,request,id):
        review = get_object_or_404(Review,id=id)
        if review.reviewer != request.user:
            return Response(
                {"error": "You can only submit your own review."},
                status=status.HTTP_403_FORBIDDEN
            )

        if review.is_submitted:
            return Response(
                {"error": "Review already submitted."},
                status=status.HTTP_400_BAD_REQUEST
            )

        review.is_submitted = True
        review.save()
        return Response(
            {"message": "Review submitted successfully."},
            status=status.HTTP_200_OK
        )


class ReviewAssigmentView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        review_assigment = ReviewAssigment.objects.all()
        paginator = BasePagination()
        page =  paginator.paginate_queryset(queryset=review_assigment,request=request)
        seralizers = ReviewAssigmentSerializer(page,many=True,context={"request":request})
        return paginator.get_paginated_response(seralizers.data)

    def post(self,request):
        seralizers = ReviewAssigmentSerializer(data=request.data,context={"request":request})
        seralizers.is_valid(raise_exception=True)
        seralizers.save()
        return Response(
            {
                "message":"Review Assigment created.",
                "data":seralizers.data
            },
            status=status.HTTP_201_CREATED
        )


class ReviewAssigmenDetailtView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,id):
        review_assigment = get_object_or_404(ReviewAssigment,id=id)
        seralizers = ReviewAssigmentSerializer(review_assigment,context={"request":request})
        return Response(
            seralizers.data,
            status=status.HTTP_200_OK
        )

    def patch(self,request,id):
        review_assigment = get_object_or_404(ReviewAssigment,id=id)
        seralizers = ReviewAssigmentSerializer(review_assigment,data=request.data,partial=True,context={"request":request})
        seralizers.is_valid(raise_exception=True)
        seralizers.save()
        return Response(
            {
                "message":"Review Assigment created.",
                "data":seralizers.data
            },
            status=status.HTTP_200_OK
        )










