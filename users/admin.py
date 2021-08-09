from django.contrib import admin

# Register your models here.

from users.models import User


class AdminUserView(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'date_joined', 'is_active',)
    list_display_links = ('username',)
    search_fields = ('firs_name', 'last_name',)


admin.site.register(User, AdminUserView)

