from django.contrib import admin
from .models import Journal, JournalRequirements, Volume


class VolumeInline(admin.TabularInline):
    model = Volume
    extra = 0
    fields = ["number","issue","year","is_published","published_date"]

class JournalRequirementsInline(admin.StackedInline):
    model = JournalRequirements
    extra = 0


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ["name","issn","is_active","created_at"]
    list_filter = ['is_active']
    search_fields = ['name','issn']
    inlines = [JournalRequirementsInline, VolumeInline]
    readonly_fields = ['created_at', 'updated_at']
    search_help_text = "Jurnal nomi yoki ISSN bo'yicha qidiring"



@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ["number","issue","year","is_published"]
    list_filter = ['is_published','year','journal']
    search_fields = ["number","issue","year"]
    readonly_fields = ['created_at', 'updated_at']



@admin.register(JournalRequirements)
class JournalRequirementsAdmin(admin.ModelAdmin):
    list_display = ['journal', 'created_at']
    readonly_fields = ['created_at', 'updated_at']


