from rest_framework import serializers
from .models import MenuCard


class MenuSerilizer(serializers.ModelSerializer):
    class Meta:
        model = MenuCard
        fields = '__all__'
