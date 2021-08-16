from django.contrib import admin

# Register your models here.
from products.models import Product, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity')
    fields = ('name', 'description',  ('price', 'quantity'), 'category',  'image',)
    readonly_fields = ('description',)
    ordering = ('quantity',)

class CategoryAdminForm(admin.ModelAdmin):
    list_display = ('name','descripton','discount',)
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('name', 'discount',)

admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)

admin.site.register(ProductCategory, CategoryAdminForm)