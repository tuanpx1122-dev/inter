from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from fruit.models import Fruit


class OrderFruitSerializer(serializers.Serializer):
    user = serializers.CharField(required=False)
    fruits = serializers.DictField(child=serializers.CharField())

    def validate_user(self, value):
        if user
        # assign user by user signing
        if value != self.context:
            raise ValidationError("User do not match with user singing")

        return value

    def validate_fruits(self, fruits_order):
        fruits_stock_qs = Fruit.objects.filter(name__in=fruits_order.keys()).values('name', 'number')
        # check number fruits order and number fruits exist in stock
        if fruits_stock_qs.count() < len(fruits_order.keys()):
            raise ValidationError("Out of stock or the store has no fruits")

        for name in fruits_order.keys():
            # map name fruit order with name fruit stock
            fruit_order = next((fruit_stock for fruit_stock in fruits_stock_qs if fruit_stock["name"] == name), None)
            # check fruit order exist in stock
            if fruit_order is None:
                raise ValidationError(f"Out of stock or the store has no this fruits {name}")
            # check number fruits order and number fruits in stock
            if fruits_order[name] > fruit_order['name']:
                raise ValidationError(f"Can only buy max is {fruit_order['name']}")

        return fruits_order

    def validate(self, value):
        user = value.get('user')
        if user is None and isinstance(self.context, AnonymousUser):
            raise ValidationError("Pls input user or signing to order")
        # check user with user signing
        if not user:
            return self.context

        return value
