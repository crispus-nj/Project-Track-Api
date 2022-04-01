from django.shortcuts import render
from django.http import JsonResponse
from rest_frameworks.decorators import api_view
from rest_framework.response import Response
from serializer import SingleSerializer, RatingSerializer
from comments.models import Single, Rating

# Create your views here.
'''
@api_view(['GET'])
def commentOverview(request):

    comment_urls = {
        'Detail View': '/project_detail',
        'Update': '/project_update',
        'Delete': '/project_delete',
    }
    return Responce(comment_urls)

@api_view(['GET'])
def ratingOverview(request):
    comment_urls = {
        'Rating': '/project_rating',
    }

return Response(comment_urls)
'''
# For single project
class SingleDetailOverview():
    query_set = Single.object.all()
    class_serializer = SingleSerializer
'''
class SingleUpdateOverview(RetrieveUpdateView):
    query_set = Single.object.all()
    class_serializer = PostCreateSerializer
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class SingleDeleteOverview(DestroySingleView):
    query_set = Single.object.all()
    class_serializer = SingleSerializer
'''
#For rating
class RatingDetailOverview():
    query_set = Single.object.all()
    class_serializer = RatingSerializer

    def perform_rating(self, serializer):
        serializer.save(user = self.request.user)

