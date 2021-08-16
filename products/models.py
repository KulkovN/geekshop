from django.db import models
from django.db.models.fields import CharField
from django.forms import ModelForm

# Create your models here.


class ProductCategory(models.Model):
    """product-category table"""
    name = models.CharField(max_length=64, unique=True)
    descripton = models.TextField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории продуктов'

    
    def __str__(self):
        return self.name


class Product (models.Model):
    """products table """
    name = models.CharField(max_length=256) 
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Прдукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}'


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name','image', 'description', 'price', 'quantity', 'category',)
       


