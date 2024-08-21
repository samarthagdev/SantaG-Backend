from rest_framework import serializers
from cosmatic.models import Cosmaticitems


class CosmaticSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Cosmaticitems
        fields = '__all__'
