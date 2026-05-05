from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Showtime, Studio, Movie
 
class ShowtimeSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()
    movie = serializers.CharField(source='movie.name', read_only=True)
    studio = serializers.CharField(source='studio.name', read_only=True)
 
    studio_id = serializers.PrimaryKeyRelatedField(
        queryset=Studio.objects.all(),
        write_only=True,
        source='studio'
    )
 
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        write_only=True,
        source='movie'
    )
 
    class Meta:
        model = Showtime
        fields = ['id', 'movie', 'studio', 'movie_id', 'studio_id', 'start_time', 'end_time', '_links']
 
    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('showtime-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('showtime-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('showtime-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('showtime-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]