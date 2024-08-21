from rest_framework import serializers
from homeview.models import OfferPoster, OfferPoster1, OfferPoster2, OfferPoster3


class OfferPosterSerilizer(serializers.ModelSerializer):
    class Meta:
        model = OfferPoster
        fields = '__all__'


class OfferPosterSerilizer1(serializers.ModelSerializer):
    class Meta:
        model = OfferPoster1
        fields = '__all__'


class OfferPosterSerilizer2(serializers.ModelSerializer):
    class Meta:
        model = OfferPoster2
        fields = '__all__'


class OfferPosterSerilizer3(serializers.ModelSerializer):
    class Meta:
        model = OfferPoster3
        fields = '__all__'
