
from rest_framework import serializers
from .models import Userdasboard


class UserdasSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Userdasboard
        fields = '__all__'
