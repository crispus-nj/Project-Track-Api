from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from users import serializers
from users.serializers import UserSerializer, AuthTokenSerializer
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    """creates a new user in the system"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES