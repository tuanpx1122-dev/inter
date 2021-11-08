from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import OrderFruitSerializer


class OrderFruitAPIView(APIView):
    def post(self, request):
        serializer = OrderFruitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)
