from django.contrib import admin
from .models import Keys,Article,Category,ArticleReferences
from casi.authors.models import Author

# Register your models here.




@admin.register(Keys)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
    search_help_text = "nom orqali qidiring"

    readonly_fields = ['created_at', 'updated_at']

@admin.register(Category)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
    search_help_text = "nom orqali qidiring"
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ArticleReferences)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["reference_name"]
    list_filter = ["reference_name"]
    search_fields = ["reference_name"]
    search_help_text = "nom orqali qidiring"

    readonly_fields = ['created_at', 'updated_at']

class ArticleReferencesInline(admin.TabularInline):
    model = ArticleReferences
    extra = 0
    fields = ['reference_name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'volume', 'language', 'status', 'article_view', 'article_download']
    list_filter = ['status', 'language', 'volume__journal']
    search_fields = ['title', 'doi', 'abstract']
    readonly_fields = ['created_at', 'updated_at', 'article_view', 'article_download']
    filter_horizontal = ['author', 'keys', 'category']
    inlines = [ArticleReferencesInline]
    list_per_page = 20
    save_on_top = True
    date_hierarchy = 'created_at'

    fieldsets = [
        ('Asosiy', {
            'fields': ['title', 'abstract', 'doi', 'language', 'pages', 'status']
        }),
        ('Fayl', {
            'fields': ['file']
        }),
        ('Bog\'lanishlar', {
            'fields': ['volume', 'author', 'keys', 'category']
        }),
        ('Statistika', {
            'fields': ['article_view', 'article_download'],
            'classes': ['collapse']
        }),
        ('Vaqt', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]
