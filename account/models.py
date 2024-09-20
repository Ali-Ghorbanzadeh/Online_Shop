from django.contrib.auth.models import User
from django.db import models
from order.models import Order
from core.models import AbstractModel


class Profile(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
