from rest_framework import serializers

from track.models import Track

class TrackSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = Track
        fields = "__all__"
