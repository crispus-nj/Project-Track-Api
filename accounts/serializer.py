from rest_framework import serializers
from .models import Account
from rest_auth.registration.serializers import RegisterSerializer

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name')
        read_only_fields = ('email',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'first_name','last_name','email']


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(Write_only = True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required = True)


    def get_cleaned_data(self):
        super(CustomRegisterSerializer,self).get_cleaned_data()

        return {
            'password' : self.validated_data.get('password', ''),
            'email' : self.validated_data.get('email', ''),
            'first_name' : self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }
