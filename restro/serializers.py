from rest_framework import serializers
from .models import Categories, Items, PreviousStoreData


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class ItemsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class PreviousDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousStoreData
        fields = '__all__'

class BothItemNCategory(serializers.Serializer):
    category = CategorySerilizer(many=True)
    item = ItemsSerilizer(many=True)
