from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status
from casi.authors.api.filters import AuthorFilter
from casi.authors.api.serializers import AuthorSerializersPrivate
from casi.authors.models import Author


class AllAuthorView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        queryset = Author.objects.all()
        filterset = AuthorFilter(request.GET, queryset=queryset)

        print("DATA:", filterset.data)  # ← shu
        print("ERRORS:", filterset.errors)  # ← shu
        print("VALID:", filterset.is_valid())  # ← shu

        if filterset.is_valid():
            queryset = filterset.qs
            print("SQL:", queryset.query)

        serializers = AuthorSerializersPrivate(queryset,many=True)
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializers = AuthorSerializersPrivate(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        res_data = {
                "message":"Author is created",
                "data":serializers.data
            }
        return Response(data=res_data,status=status.HTTP_201_CREATED)


class AuthorDetailView(APIView):
    permission_classes = [AllowAny]
    def get_author(self,id):
        return get_object_or_404(Author,id=id)
    def get(self,request,id):
        serializers = AuthorSerializersPrivate(self.get_author(id))
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def put(self, request, id):
        serializers = AuthorSerializersPrivate(self.get_author(id),data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        res_data = {
                "message": "Author is updated",
                "data": serializers.data
            }
        return Response(data=res_data,status=status.HTTP_200_OK)



    def patch(self, request, id):
        serializers = AuthorSerializersPrivate(self.get_author(id), data=request.data,partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        res_data = {
                "message": "Author is updated",
                "data": serializers.data
            }
        return Response(data=res_data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        self.get_author(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
