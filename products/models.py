from django.db import models
from django.db.models.fields import CharField
from django.forms import ModelForm

# Create your models here.


class ProductCategory(models.Model):
    """product-category table"""
    name = models.CharField(max_length=64, unique=True)
    descripton = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории продуктов'

    

    def __str__(self):
        return self.name


class Product (models.Model):
    """products table """
    name = models.CharField(max_length=256)  # имя товара
    # хранение изображения
    image = models.ImageField(upload_to='products_images', blank=True)
    # описание товара
    description = models.CharField(max_length=64, blank=True)
    # хранение стоимости товара
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # задаем начальное значение стоимости, ниже которого оно не может опуститься
    quantity = models.PositiveIntegerField(default=0)
    # задаем ключ-ссылку на таблицу ProductCategory
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
       


