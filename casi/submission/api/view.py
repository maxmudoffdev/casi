from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework import status
from casi.common.paginator import BasePagination
from casi.submission.api.serializers import SubmissionSerializers
from casi.submission.api.state_machine import transition_status
from casi.submission.models import Submission, SubmissionStatus


class AllSubmissionView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        submission = Submission.objects.all().filter(is_active=True)
        paginator = BasePagination()
        page = paginator.paginate_queryset(queryset=submission,request=request)
        serializers = SubmissionSerializers(page,many=True, context={"request": request} )
        return paginator.get_paginated_response(serializers.data)


    def post(self,request):
        serailizers = SubmissionSerializers(data=request.data, context={"request": request} )
        serailizers.is_valid(raise_exception=True)
        serailizers.save()
        return Response(
            {
                "message":"Submission created",
                "data":serailizers.data
            },
            status=status.HTTP_201_CREATED
        )

class SubmissionDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,id):
        submission = get_object_or_404(Submission,id=id)
        seralizers = SubmissionSerializers(submission,context={"request": request})
        return Response(
            seralizers.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, id):
        submission = get_object_or_404(Submission, id=id)
        seralizers = SubmissionSerializers(submission,data=request.data,partial=True,context={"request": request})
        seralizers.is_valid(raise_exception=True)
        seralizers.save()
        return Response(
            {
                "message":"Submission updated",
                "data":seralizers.data
            },
            status=status.HTTP_200_OK
        )
    def delete(self,request,id):
        submission = get_object_or_404(Submission, id=id)
        submission.is_active = False
        submission.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SubmissionTransitionView(APIView):
    permission_classes = [AllowAny]
    transition_to = None
    def post(self,request,id):
        submission = get_object_or_404(Submission,id=id)
        try:
            transition_status(submission,self.transition_to)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"message": f"Status changed to {self.transition_to}"},
            status=status.HTTP_200_OK
        )



class SubmissionSubmitView(SubmissionTransitionView):
    transition_to = SubmissionStatus.SUBMITTED

class SubmissionUnderReviewView(SubmissionTransitionView):
    transition_to = SubmissionStatus.UNDER_REVIEW

class SubmissionAcceptView(SubmissionTransitionView):
    transition_to = SubmissionStatus.ACCEPTED

class SubmissionRejectView(SubmissionTransitionView):
    transition_to = SubmissionStatus.REJECTED

class SubmissionRevisionView(SubmissionTransitionView):
    transition_to = SubmissionStatus.REVISION_REQUESTED

class SubmissionPublishView(SubmissionTransitionView):
    transition_to = SubmissionStatus.PUBLISHED
