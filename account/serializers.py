from rest_framework import serializers
from .models import Account


class AccountSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


