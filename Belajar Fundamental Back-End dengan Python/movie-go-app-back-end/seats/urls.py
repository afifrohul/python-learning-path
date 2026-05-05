from django.urls import path
from . import views
 
urlpatterns = [
  path('seats/', views.SeatListCreateView.as_view(), name='seat-list'),
  path('seats/<uuid:pk>/', views.SeatDetailView.as_view(), name='seat-detail'),
]
