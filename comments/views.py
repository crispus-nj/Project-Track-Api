import imp
from django.shortcuts import render
from rest_framework import viewsets
from .models import Single, Rating
from serializers import SingleSerializer, RatingSerializer

# Create your views here.

class SingleView(viewsets.ModelViewSet):
    queryset = Single.objects.all()
    serializer_class = SingleSerializer



class RatingView(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
