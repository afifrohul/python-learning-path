from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Seat, Studio
 
class SeatSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()
    studio = serializers.CharField(source='studio.name', read_only=True)
    studio_id = serializers.PrimaryKeyRelatedField(
        queryset=Studio.objects.all(),
        write_only=True,
        source='studio'
    )
 
    class Meta:
        model = Seat
        fields = ['id', 'studio', 'studio_id', 'seat_number', '_links']
 
    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('seat-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('seat-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('seat-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('seat-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]