from django.contrib import admin
from django.db import models

# # Register your models here.

from .models import Order, OrderItem


class AdminOrderView(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated',)
    list_display_links = ('user', 'created')
    search_fields = ('user', 'created', )


class AdminOIView(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity',)
    list_display_links = ('order', 'product',)
    search_fields = ('order',)


admin.site.register(Order, AdminOrderView)
admin.site.register(OrderItem, AdminOIView)
