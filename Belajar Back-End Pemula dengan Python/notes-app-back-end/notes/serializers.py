from rest_framework import serializers
from rest_framework.reverse import reverse
from notes.models import Note
 
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()
 
    class Meta:
        model = Note
        fields = ['id', 'title', 'body', 'tags', 'createdAt', 'updatedAt', '_links']
 

    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('note-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('note-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('note-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            }
        ]
