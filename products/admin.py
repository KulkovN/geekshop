from django.contrib import admin

# Register your models here.
from products.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity')
    fields = ('name', 'description',  ('price', 'quantity'), 'category',  'image',)
    readonly_fields = ('description',)
    ordering = ('quantity',)

class CategoryAdminForm(admin.ModelAdmin):
    class Meta:
        list_display = ('name','descripton',)
        list_display_links = ('name','descripton',)
        search_fields = ('name',)
        ordering = ('name',)


admin.site.register(ProductCategory, CategoryAdminForm)