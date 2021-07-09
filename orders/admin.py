from django.contrib import admin
from django.db import models

# # Register your models here.

from .models import Order


class AdminOrderView(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated',)
    list_display_links = ('user', 'created')
    search_fields = ('user', 'created', )


admin.site.register(Order, AdminOrderView)
