from rest_framework import serializers
from broadcast.models import Otpveification,Otpveification1
from account.models import Account
import random

class OtpSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Otpveification
        fields = '__all__'

class OtpSerilizer1(serializers.ModelSerializer):

    class Meta:
        model = Otpveification1
        fields = '__all__'

class UserRegistration(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['userName', 'number', 'password']

    def save(self):
        account = Account(
            userName=self.validated_data['userName'],
            number=self.validated_data['number']
        )

        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account