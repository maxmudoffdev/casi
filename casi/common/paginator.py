from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status


class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 100


    def get_paginated_response(self,data):
        return Response({
            "meta":{
                "total":self.page.paginator.count,
                "page":self.page.number,
                "page_size":self.get_page_size(self.request),
                "total_page":self.page.paginator.num_pages,
                "has_next": self.page.has_next(),
                "has_previous": self.page.has_previous(),
                "status":status.HTTP_200_OK

            },
            "data":data
        })
