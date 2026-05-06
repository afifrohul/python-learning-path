from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Reservation, ReservedSeat, Showtime, Seat
from core.models import User
class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()
    user = serializers.CharField(source='user.username', read_only=True)
    showtime = serializers.CharField(source='showtime.id', read_only=True)
    showtime_id = serializers.PrimaryKeyRelatedField(
        queryset=Showtime.objects.all(),
        write_only=True,
        source='showtime'
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='user'
    )
    class Meta:
        model = Reservation
        fields = ['id', 'user', 'showtime', 'user_id', 'showtime_id', 'amount', 'reserved_at', '_links']
    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('reservation-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('reservation-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('reservation-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('reservation-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]
class ReservedSeatSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()
    seat = serializers.CharField(source='seat.id', read_only=True)
    showtime = serializers.CharField(source='showtime.id', read_only=True)
    reservation = serializers.CharField(source='reservation.id', read_only=True)
    seat_id = serializers.PrimaryKeyRelatedField(
        queryset=Seat.objects.all(),
        write_only=True,
        source='seat'
    )
    showtime_id = serializers.PrimaryKeyRelatedField(
        queryset=Showtime.objects.all(),
        write_only=True,
        source='showtime'
    )
    reservation_id = serializers.PrimaryKeyRelatedField(
        queryset=Reservation.objects.all(),
        write_only=True,
        source='reservation'
    )
    class Meta:
        model = ReservedSeat
        fields = ['id', 'seat', 'showtime', 'reservation', 'seat_id', 'showtime_id', 'reservation_id', '_links']
    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('reserved-seat-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('reserved-seat-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('reserved-seat-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('reserved-seat-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]
