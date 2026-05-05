from django.urls import path
from . import views
 
urlpatterns = [
  path('studios/', views.StudioListCreateView.as_view(), name='studio-list'),
  path('studios/<uuid:pk>/', views.StudioDetailView.as_view(), name='studio-detail'),
  path('studio-managers/', views.StudioManagerListCreateView.as_view(), name='studio-manager-list'),
  path('studio-managers/<uuid:pk>/', views.StudioManagerDetailView.as_view(), name='studio-manager-detail'),
]
