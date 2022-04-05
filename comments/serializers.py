from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Single, Rating


class SingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Single
        field = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        field = '__all__'
