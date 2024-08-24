from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from . models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'nama', 'is_staff']

    fieldsets = (
        (None, {'fields': ['email', 'nama', 'password',]}),
        ('Personal Info', {'fields': ['tmp_lahir', 'tgl_lahir', 'no_hp',]}),
        ('Permissions', {'fields': [
         'groups', 'is_active', 'is_staff', 'is_superuser',]}),
    )

    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['nama', 'email', 'password1', 'password2'],
            },
        )
    ]


admin.site.register(User, UserAdmin)
