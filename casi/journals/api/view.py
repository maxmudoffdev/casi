from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from casi.journals.api.filters import JournalFilter
from casi.journals.api.serializers import JournalSerialziers, VolumeSerialziers,JournalRequirementsSerilizers
from casi.journals.models import Journal, Volume,JournalRequirements
from casi.journals.pagination import JournalPagination


class AllJournalView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        journal = Journal.objects.all()
        filterset = JournalFilter(request.GET,queryset=journal)
        if filterset.is_valid():
            journal = filterset.qs
        paginator = JournalPagination()
        page = paginator.paginate_queryset(journal,request)
        serializers = JournalSerialziers(page,many=True,context={"request": request})
        return paginator.get_paginated_response(serializers.data)

    def post(self, request):
        serializers = JournalSerialziers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(
            {
                "message": "Journal created",
                "data": serializers.data
            },
            status=status.HTTP_201_CREATED
        )
class JournalDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,slug):
        journal = get_object_or_404(Journal,slug=slug)
        seralizers = JournalSerialziers(journal)
        return Response(
            seralizers.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, slug):
        journal = get_object_or_404(Journal, slug=slug)
        seralizers = JournalSerialziers(journal,data=request.data,partial=True,context={"request": request})
        seralizers.is_valid(raise_exception=True)
        seralizers.save()

        return Response(
            {
                "message": "Journal updated",
                "data": seralizers.data
            },

            status=status.HTTP_200_OK
        )
    def delete(self, request, slug):
        journal = get_object_or_404(Journal, slug=slug)
        journal.is_active = False
        journal.save()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class VolumeView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        journal_slug = request.query_params.get("journal")

        volume = Volume.objects.all()
        if journal_slug:
            volume = volume.filter(journal_slug=journal_slug)
        seralizers = VolumeSerialziers(volume,many=True)
        return Response(
            seralizers.data
        )

    def post(self,request):
        serializers = VolumeSerialziers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(
            {"message": "Volume created", "data": serializers.data},
            status=status.HTTP_201_CREATED
        )

class VolumeViewDetail(APIView):
    permission_classes = [AllowAny]
    def get(self,request,id):
        volume = get_object_or_404(Volume,id=id)
        serialziers = VolumeSerialziers(volume)
        return Response(serialziers.data)

    def patch(self, request, id):
        volume = get_object_or_404(Volume, id=id)
        serialziers = VolumeSerialziers(volume,data=request.data,partial=True)
        serialziers.is_valid()
        serialziers.save()
        return Response({
            "message":"Volume updated",
            "data":serialziers.data},
            status=status.HTTP_200_OK
        )

    def delete(self, request, id):
        volume = get_object_or_404(Volume, id=id)
        volume.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class VolumeView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        journal_slug = request.query_params.get("journal")

        volume = Volume.objects.all()
        if journal_slug:
            volume = volume.filter(journal_slug=journal_slug)
        seralizers = VolumeSerialziers(volume,many=True)
        return Response(
            seralizers.data
        )

    def post(self,request):
        serializers = VolumeSerialziers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(
            {"message": "Volume created", "data": serializers.data},
            status=status.HTTP_201_CREATED
        )
class JournalRequirementsView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        journal_requirements = JournalRequirements.objects.all()
        serializers = JournalRequirementsSerilizers(journal_requirements)
        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request):
        seralziers = JournalRequirementsSerilizers(data=request.data)
        seralziers.is_valid(raise_exception=True)
        print(seralziers.validated_data)  # ← qo'shing

        seralziers.save()
        return Response(
            {
                "message":"JournalRequirements is created",
                "data":seralziers.data
            },
            status=status.HTTP_201_CREATED
        )

class JournalRequirementsDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self,request,id):
        journal_requirements = get_object_or_404(JournalRequirements,id=id)
        serializers = JournalRequirementsSerilizers(journal_requirements)
        return Response(serializers.data,status=status.HTTP_200_OK)


    def patch(self,request,id):
        journal_requirements = get_object_or_404(JournalRequirements,id=id)
        serializers = JournalRequirementsSerilizers(journal_requirements,data=request.data,partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {
                "message": "JournalRequirements is updated",
                "data": serializers.data
            },
            status=status.HTTP_200_OK
        )

    def delete(self,request,id):
        journal_requirements = get_object_or_404(JournalRequirements,id=id)
        journal_requirements.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

