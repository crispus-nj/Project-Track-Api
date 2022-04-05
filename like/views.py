from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import LikeSerializer
from .models import Like

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer