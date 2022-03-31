from django.shortcuts import render
from django.http import JsonResponse
from rest_frameworks.decorators import api_view
from rest_framework.response import Response
from serializer import SingleSerializer

# Create your views here.

@api_view(['GET'])
def commentOverview(request):

    comment_urls = {
        'Detail View': '/project_detail',
        'Update': '/project_update',
        'Delete': '/project_delete',
    }
    return Responce(comment_urls)
