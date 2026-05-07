from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Movie, MoviePoster
 
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()
 
    class Meta:
        model = Movie
        fields = ['id', 'name', 'overview', 'release_date', 'country', 'language',
                  'producer', 'director', 'duration', 'genre', '_links']
 
    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('movie-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('movie-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('movie-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('movie-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]

class MoviePosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePoster
        fields = ['id', 'movie', 'image']
 
    def validate_image(self, value):
        max_size = 2 * 1024 * 1024  # 2MB
        if value.size > max_size:
            raise serializers.ValidationError("Image size cannot exceed 2MB.")
        return value