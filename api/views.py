from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def api_routes(request):
    urls = [
        "GET https://project-track-api.herokuapp.com/api/projects/",
        "GET https://project-track-api.herokuapp.com/api/track/",
        "GET https://project-track-api.herokuapp.com/api/like-api/",
        "GET https://project-track-api.herokuapp.com/api/users/",
        "GET https://project-track-api.herokuapp.com/api/single-project/",
    ]
    return Response(urls, status=status.HTTP_202_ACCEPTED)