from django.urls import path
from . import views
urlpatterns = [
  path('reservations/', views.ReservationListCreateView.as_view(), name='reservation-list'),
  path('reservations/<uuid:pk>/', views.ReservationDetailView.as_view(), name='reservation-detail'),
  path('reserved-seats/', views.ReservedSeatListCreateView.as_view(), name='reserved-seat-list'),
  path('reserved-seats/<uuid:pk>/', views.ReservedSeatDetailView.as_view(), name='reserved-seat-detail'),
]
