
from rest_framework import serializers

from accounts.models import Account
from .models import Single, Rating
from projects.serializers import ProjectSerializer
from users.serializers import UserSerializer


class SingleSerializer(serializers.ModelSerializer):
    # user = ProjectSerializer(read_only=True)
    # user_id=serializers.IntegerField()
    class Meta:
        model = Single
        fields = '__all__'

# class RecipeMainSerializer(serializers.ModelSerializer):
#     ingredients = UserSerializer(many=True)

#     class Meta:
#         model = Single
#         fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'





