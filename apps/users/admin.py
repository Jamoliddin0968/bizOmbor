from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_staff", "is_active",'is_manager')
    list_filter = ("username", "is_staff", "is_active",'is_manager')
    fieldsets = (
        (None, {"fields": ("username",'password','is_manager','first_name','last_name')}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password",'is_manager'
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)
    readonly_fields = ('password',)
