from rest_framework import serializers

from track.models import Track

class TrackSerializer(serializers.ModelSerializer):
    # track = serializers.SlugRelatedField(
    #     slug_field='isbn13',
    #     queryset=Track.objects.all()
    #     )
    class Meta:
        model = Track
        fields = ['name']
