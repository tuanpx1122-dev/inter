from django.contrib.auth.models import AbstractUser
from django.db import models

from fruit.models import Fruit


class Order(models.Model):
    fruit = models.ForeignKey(Fruit, on_delete=models.SET_NULL, null=True)
    number = models.PositiveIntegerField(verbose_name='number fruit order', default=0)


# Create your models here.
class Users(AbstractUser):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
