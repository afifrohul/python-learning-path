from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Ticket
from events.models import Event

class TicketSerializer(serializers.HyperlinkedModelSerializer):
  _links = serializers.SerializerMethodField()

  event = serializers.CharField(source='event.name', read_only=True)

  event_id = serializers.PrimaryKeyRelatedField(
    queryset=Event.objects.all(),
    write_only=True,
    source='event'
  )

  class Meta:
    model = Ticket
    fields = ['id', 'name', 'price', 'sales_start', 'sales_end', 'quota', 'event_id', 'event', '_links']

  def get__links(self, obj):
    request = self.context.get('request')
    return [
      {
        "rel": "self",
        "href": reverse('ticket-list', request=request),
        "action": "POST",
        "types": ["application/json"]
      },
      {
        "rel": "self",
        "href": reverse('ticket-detail', kwargs={'pk': obj.pk}, request=request),
        "action": "GET",
        "types": ["application/json"]
      },
      {
        "rel": "self",
        "href": reverse('ticket-detail', kwargs={'pk': obj.pk}, request=request),
        "action": "PUT",
        "types": ["application/json"]
      },
      {
        "rel": "self",
        "href": reverse('ticket-detail', kwargs={'pk': obj.pk}, request=request),
        "action": "DELETE",
        "types": ["application/json"]
      }
    ]