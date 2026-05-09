from django_filters import FilterSet,CharFilter
from casi.authors.models import Author
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q
from rest_framework.validators import ValidationError


class AuthorFilter(FilterSet):
    q = CharFilter(method="search_authors",label="Qidiruv (Ism, Familiya, ORCID)")

    affiliation = CharFilter(
        field_name="affiliation",
        lookup_expr="icontains"

    )

    def search_authors(self,queryset,name,value):
        if len(value) > 100:
            raise ValidationError("Search query too long.")
        if not value:
            return queryset

        if len(value) < 3:
            return queryset.filter(
                Q(first_name__icontains=value) |
                Q(last_name__icontains=value) |
                Q(orc_id__icontains=value)
            )

        return (
            queryset.annotate(
                first_name_sim=TrigramSimilarity("first_name",value),
                last_name_sim=TrigramSimilarity("last_name", value),

        ).filter(
                Q(first_name_sim__gt=0.3)|
                Q(last_name_sim__gt=0.3)|
                Q(orc_id__icontains=value)
            ).order_by("-first_name_sim","-last_name_sim")
        )




    class Meta:
        model = Author
        fields = ['affiliation']

