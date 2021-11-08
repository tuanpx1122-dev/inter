from rest_framework import serializers

from fruit.models import Fruit





class OrderFruitSerializer(serializers.Serializer):
    user = serializers.CharField(allow_null=True)
    fruits = FruitSerializer(many=True)

    def validate_user(self, value):
        if not value:
            return self.user
        if value != self.user:
            raise ValueError('User diff')
