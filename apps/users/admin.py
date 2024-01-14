from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'is_manager')
    list_filter = ('is_manager',)

    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'is_manager')}),
        # ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
from .models import Seans,UserTarif

admin.site.register((Seans,UserTarif))
# Register your models here.
