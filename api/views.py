from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def api_routes(request):
    urls = [
        "GET http://127.0.0.1:8000/api/projects/",
        "GET http://127.0.0.1:8000/api/like-api/",
        "GET http://127.0.0.1:8000/api/users/",
        "GET http://127.0.0.1:8000/api/single-project/",
    ]
    return Response(urls, status=status.HTTP_202_ACCEPTED)