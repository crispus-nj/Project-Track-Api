from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.
class ProjectView(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    serializer_class= ProjectSerializer

class Projects(APIView):    
    def post(self, request, *args,):
        track = request.data.get('track')
        print(track)
        if track is not None:
            projects = Project.objects.filter(track_id=track)
            print(projects)
            result = ProjectSerializer(projects, many=True)
            return Response(result.data, status=200)
        else: 
            projects = Project.objects.all()
            result = ProjectSerializer(projects, many=True)
            return Response(result.data, status=200)   