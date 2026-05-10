from django.core.exceptions import ValidationError
from django_filters import FilterSet,CharFilter
from django.db.models import Q

from casi.journals.models import Journal


class JournalFilter(FilterSet):
    q = CharFilter(method="search_journals",label="Search journal name and issn")
    journal_name = CharFilter(
        field_name="name",
        lookup_expr="icontains"
    )

    def search_journals(self,queryset,name,value):
        if not value:
            return queryset

        if len(value) > 100:
            raise ValidationError("Search query too long.")

        return queryset.filter(
            Q(name__icontains=value)|
            Q(issn__icontains=value)
        )

    class Meta:
        model = Journal
        fields = ['name']
