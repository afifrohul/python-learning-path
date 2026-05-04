from django.urls import path
from . import views
 
urlpatterns = [
  path('notes/',views.NoteList.as_view(), name='note-list'),
  path('notes/<uuid:pk>/', views.NoteDetail.as_view(), name='note-detail')
]