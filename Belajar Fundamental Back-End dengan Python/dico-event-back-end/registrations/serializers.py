from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Registration
from tickets.models import Ticket
from core.models import User

class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
  _links = serializers.SerializerMethodField()

  ticket = serializers.CharField(source='ticket.name', read_only=True)
  user = serializers.CharField(source='user.username', read_only=True)

  ticket_id = serializers.PrimaryKeyRelatedField(
    queryset=Ticket.objects.all(),
    write_only=True,
    source='ticket'
  )

  user_id = serializers.PrimaryKeyRelatedField(
    queryset=User.objects.all(),
    write_only=True,
    source='user'
  )

  class Meta:
    model = Registration
    fields = ['id', 'ticket', 'ticket_id', 'user', 'user_id', '_links']

  def get__links(self, obj):
    request = self.context.get('request')
    return [
      {
        "rel": "self",
        "href": reverse('registration-list', request=request),
        "action": "POST",
        "types": ["application/json"]
      },
      {
        "rel": "self",
        "href": reverse('registration-detail', kwargs={'pk': obj.pk}, request=request),
        "action": "GET",
        "types": ["application/json"]
      },
      {
        "rel": "self",
        "href": reverse('registration-detail', kwargs={'pk': obj.pk}, request=request),
        "action": "PUT",
        "types": ["application/json"]
      },
      {
        "rel": "self",
        "href": reverse('registration-detail', kwargs={'pk': obj.pk}, request=request),
        "action": "DELETE",
        "types": ["application/json"]
      }
    ]