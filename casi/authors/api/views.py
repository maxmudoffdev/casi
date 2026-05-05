from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status

from casi.authors.api.serializers import AuthorSerializers
from casi.authors.models import Author


class AllAuthorView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        author = Author.objects.all()
        serializers = AuthorSerializers(author,many=True)
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializers = AuthorSerializers(data=request.data)
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
        serializers = AuthorSerializers(self.get_author(id))
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def put(self, request, id):
        serializers = AuthorSerializers(self.get_author(id),data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        res_data = {
                "message": "Author is updated",
                "data": serializers.data
            }
        return Response(data=res_data,status=status.HTTP_200_OK)



    def patch(self, request, id):
        serializers = AuthorSerializers(self.get_author(id), data=request.data,partial=True)
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
