from .models import CartItem
from rest_framework import serializers


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = ('user', 'product', 'quantity')
