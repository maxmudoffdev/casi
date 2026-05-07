from django.contrib import admin

from casi.authors.models import Author


# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","email","orc_id"]
    list_filter = ["email","first_name","last_name"]
    search_fields = ["first_name","last_name","orc_id","email"]
    search_help_text = "Ism va familiya yoki orcid orqali qidiring"
    readonly_fields = ['created_at', 'updated_at']


