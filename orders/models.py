from django.db import models

# # Create your models here.

from django.conf import settings
from django.db import models

from products.models import Product


class Order(models.Model):
    STATUS = (
        ('CRE', 'Создание'),
        ('PD', 'Оплачен'),
        ('RDE', 'Готов к выдаче'),
        ('UPD', 'Обнволен'),
        ('CNL', 'Отменён'),
        ('DRD', 'Выдан')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Cоздан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Oбновлён')
    is_active = models.BooleanField(default=True)

    status = models.CharField(
        choices=STATUS, default="CRE", verbose_name='Cтатус', max_length=3)

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['created']

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        total_quantity = sum([i.quantity for i in items])
        return total_quantity

    def get_total_cost(self):
        items = self.orderitems.select_related()
        total_cost = sum([i.quantity * i.product.price for i in items])
        return total_cost

    def delete(self, using=None, keep_parents=False):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()
        self.is_active = False
        self.save()



class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name='количество')

    def get_product_cost(self):
        return self.product.price * self.quantity
