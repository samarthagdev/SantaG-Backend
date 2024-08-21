from rest_framework import serializers
from .models import BagAdding, Bagitems, AddToCart, FullOrder




class BagAddingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = BagAdding
        fields = '__all__'


class BagitemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Bagitems
        fields = '__all__'

class AddtoCartSerilizer(serializers.ModelSerializer):
    class Meta:
        model = AddToCart
        fields = '__all__'

class FullOrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = FullOrder
        fields = '__all__'