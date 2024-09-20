from django.contrib.auth.models import User
from django.db import models
from product.models import Product
from core.models import AbstractModel


class Order(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'


class OrderItem(AbstractModel):
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='orders')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return f'#{self.item.name} {self.quantity} ${self.total_price}'
