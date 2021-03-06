from django.db import models
from django.utils.functional import cached_property

# Create your models here.
from users.models import User
from products.models import Product

# работа с остатками товара через использование менеджера объектов
class BasketQuerySet(models.QuerySet):

    def delete(self):
        for item in self:
            item.product.quantity += item.quantity
            item.product.save()
        super().delete()

class Basket(models.Model):
    # определение менеджера объектов  в модели
    objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_items_cached
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_items_cached
        return sum(basket.sum() for basket in baskets)

    # работа с остатками товара через использование сигналов
    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)

    # переопределение методов delete и save для менеджера объектов
    def delete(self, *args, **kwargs):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.objects.get(pk=self.pk).quantity

        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)
        