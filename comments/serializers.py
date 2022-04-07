from rest_framework import serializers
from .models import Single, Rating


class SingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Single
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
