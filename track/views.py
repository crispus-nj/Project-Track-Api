from rest_framework import viewsets
from .serializers import TrackSerializer
from .models import Track

# Create your views here.
class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

# Create your views here.
