from django.db import models


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(verbose_name='name fruit', max_length=255, unique=True)
    number = models.PositiveIntegerField(verbose_name='number fruit present', default=0)

