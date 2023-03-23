from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import ImageUpload, RoomModels,MessageModels
from .models import UserPostList
from .models import Post
# from .models import Account
# admin.site.register(Account)
admin.site.register(ImageUpload)
admin.site.register(UserPostList)
admin.site.register(Post)


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
        ('Permissions', {'fields': ('staff', 'admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('loginID', 'password1', 'password2')}
        ),
    )

admin.site.register(RoomModels)
admin.site.register(MessageModels)
