from rest_framework import serializers
from .models import Address


class AddressSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


