from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Project
from track.serializers import TrackSerializer

class ProjectSerializer(serializers.ModelSerializer):
    track = TrackSerializer(read_only=True)
    track_id = serializers.IntegerField()
    
    class Meta:
        model= Project
        fields = '__all__'