from django_filters import FilterSet,CharFilter
from casi.authors.models import Author
from django.contrib.postgres.search import TrigramSimilarity


class AuthorFilter(FilterSet):
    q = CharFilter(method="Search_authors",label="Qidiruv (Ism, Familiya, ORCID)")
    class Meta:
        model = Author
        fields = ['q','orc_id']
