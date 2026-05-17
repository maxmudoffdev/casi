# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from casi.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    list_display = ["email", "first_name", "last_name", "role", "is_active", "telegram_verified"]
    search_fields = ["email", "first_name", "last_name"]
    list_filter = ["role", "is_active", "telegram_verified"]
    show_full_result_count = False

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Role", {"fields": ("role",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Telegram", {"fields": (
            "telegram_chat_id",
            "telegram_verified",
            "telegram_verification_code",
            "telegram_code_expires",
            "telegram_token",
            "telegram_token_expires",
        )}),
        ("Verification", {"fields": (
            "verification_token",
            "verification_token_expires",
            "email_verified",
            "verification_method",
        )}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2"),
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request)
