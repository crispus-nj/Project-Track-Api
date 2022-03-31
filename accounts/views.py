from django.shortcuts import render
from .models import Account
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response

# Create your views here.


class CustomRegisterView(RegisterView):
    queryset = Account.objects.all()


class UserAPIView(APIView):
    @staticmethod
    def get(request):
        users = Account.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)