from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_staff", "is_active",)
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)
