from rest_framework import serializers
from comments.models import Single


class SingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Single
        fields = '__all__'
