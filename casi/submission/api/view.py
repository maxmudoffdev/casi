from rest_framework.permissions import AllowAny
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework import status
from casi.common.paginator import BasePagination
from casi.submission.api.serializers import SubmissionSerializers
from casi.submission.models import Submission


class AllSubmissionView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        submission = Submission.objects.all()
        paginator = BasePagination()
        page = paginator.paginate_queryset(queryset=submission,request=request)
        serializers = SubmissionSerializers(page,many=True)
        return paginator.get_paginated_response(serializers.data)


    def post(self,request):
        serailizers = SubmissionSerializers(data=request.data)
        serailizers.is_valid(raise_exception=True)
        serailizers.save()
        return Response(
            {
                "message":"Submission created",
                "data":serailizers.data
            },
            status=status.HTTP_201_CREATED
        )
