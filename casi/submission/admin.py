from django.contrib import admin
from casi.submission.models import Submission
# Register your models here.

@admin.register(Submission)
class ModelNameAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "title",
        "abstract",
        "file",
        "keyword",
        "journal",
        "author",
        "cover_letter",
        "status",
        "doi",
        "submitted_by",

    )
    list_display = ["id","title","journal"]
    list_filter = ["status", "journal"]
    readonly_fields = ["id", "doi", "status"]
    search_fields = ["title","doi"]



