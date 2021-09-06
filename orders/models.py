from django.db import models
from django.utils.functional import cached_property
# # Create your models here.

from django.conf import settings
from django.db import models

from products.models import Product
# from baskets.models import Basket


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STR'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RD'
    CANCEL = 'CNC'
    DELIVERED = 'DVD'

    STATUS = (
        (FORMING, 'Формируется'),
        (SENT_TO_PROCEED, 'Отправлен в обработку'),
        (PROCEEDED, 'Обработан'),
        (PAID, 'Оплачен'),
        (READY, 'Готов к выдаче'),
        (CANCEL, 'Отменён'),
        (DELIVERED, 'Выдан')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Cоздан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Oбновлён')
    is_active = models.BooleanField(default=True)

    status = models.CharField(
        choices=STATUS, default=FORMING, verbose_name='Cтатус', max_length=3)

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['created']


    @cached_property
    def items_cached(self):
        return self.orderitems.select_related()


    def get_total_quantity(self):
        items = self.orderitems.select_related()
        total_quantity = sum([i.quantity for i in items])
        return total_quantity

    def get_total_cost(self):
        items = self.orderitems.select_related()
        total_cost = sum([i.quantity * i.product.price for i in items])
        return total_cost


    def get_summary(self):
        items = self.items_cached
        return {
            'total_cost': sum(list(map(lambda x: x.quantity * x.product.price, items))),
            'total_quantity': sum(list(map(lambda x: x.quantity, items)))
        }


    def delete(self, using=None, keep_parents=False):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()
        self.is_active = False
        self.save()

    @staticmethod
    def get_item(pk):
        return Order.objects.get(pk=pk)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name='количество')

    class Meta:
        verbose_name_plural = 'Элементы заказов'
        verbose_name = 'Элемент'
        ordering = ['order']

    def get_product_cost(self):
        return self.product.price * self.quantity
