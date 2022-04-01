from rest_framework import generics,authentication,permissions
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

class ManageUserView(generics.RetrieveAPIView):
    """manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permissions_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.users