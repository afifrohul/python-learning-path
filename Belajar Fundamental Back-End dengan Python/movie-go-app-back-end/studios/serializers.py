from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Studio, StudioManager
from core.models import User
 
class StudioSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()
 
    class Meta:
        model = Studio
        fields = ['id', 'name', 'seat_capacity', '_links']
 
    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('studio-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('studio-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('studio-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('studio-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]
 
class StudioManagerSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='user'
    )
    studio_id = serializers.PrimaryKeyRelatedField(
        queryset=Studio.objects.all(),
        write_only=True,
        source='studio'
    )
 
    user = serializers.CharField(source='user.username', read_only=True)
    studio = serializers.CharField(source='studio.name', read_only=True)
 
    class Meta:
        model = StudioManager
        fields = ['id', 'user_id', 'studio_id', 'user', 'studio', '_links']
 
    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('studio-manager-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('studio-manager-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('studio-manager-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('studio-manager-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]