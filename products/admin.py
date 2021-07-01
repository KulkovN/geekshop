from django.contrib import admin

# Register your models here.
from products.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity')
    fields = ('name', 'description',  ('price', 'quantity'), 'category',  'image',)
    readonly_fields = ('description',)
    ordering = ('quantity',)