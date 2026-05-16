from django.contrib import admin

from casi.reviews.models import Review, ReviewAssigment


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["submission","reviewer","recommendation"]
    list_filter = ["recommendation"]
    search_fields = ["submission__title", "reviewer__username"]
    readonly_fields = ["id","created_at", "updated_at"]
    show_full_result_count = False

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            "submission", "reviewer"
        )


@admin.register(ReviewAssigment)
class ReviewerAssignmentAdmin(admin.ModelAdmin):
    list_display = ["submission", "reviewer", "asigment_by", "deadline", "status"]
    list_filter = ["status"]
    search_fields = ["submission__title", "reviewer__reviewer__username"]
    readonly_fields = ["id", "created_at", "updated_at"]
    show_full_result_count = False

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            "submission", "reviewer", "asigment_by"
        )



