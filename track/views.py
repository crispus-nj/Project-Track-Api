from rest_framework import viewsets
from .serializers import TrackSerializer
from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import Track

# Create your views here.
class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

# Create your views here.
class getTracks(APIView):
    def get(self, request, *args, **kwargs):
        results = Track.objects.all()
        serializedResults = TrackSerializer(results, many=True)
        return Response(serializedResults.data, status=200)

