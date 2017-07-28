from django.contrib import admin

from version1.models import UserDetail


class UserDetailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'name',
        'contact_number',
        'gender',
        'date_of_birth',
    )

    list_filter = (
        'gender',
    )


admin.site.register(UserDetail, UserDetailAdmin)