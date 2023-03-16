from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
# from .models import Account
# admin.site.register(Account)

class UserAdmin(BaseUserAdmin):
    
    list_display = (
        "loginID",
        "active",
        "staff",
        "admin",
    )
    list_filter = (
        "admin",
        "active",
    )
    filter_horizontal = ()
    ordering = ("loginID",)
    search_fields = ('loginID',)

    fieldsets = (
        (None, {'fields': ('loginID', 'password')}),
        ('Permissions', {'fields': ('staff','admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('loginID', 'password1', 'password2')}
        ),
    )

admin.site.register(User, UserAdmin)