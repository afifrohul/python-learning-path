from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404
from .models import Event
from .serializers import EventSerializer
from core.permissions import IsAdminOrSuperUser

# Create your views here.
class EventListCreateView(APIView):
  authentication_classes = [JWTAuthentication]

  def get_permissions(self):
    if self.request.method == 'POST':
      return [IsAuthenticated(), IsAdminOrSuperUser()]
    return [IsAuthenticated()]
  
  def get(self, request):
    events = Event.objects.all().order_by('name')[:10]
    serializer = EventSerializer(events, many=True)
    return Response({'events': serializer.data})
  
  def post(self, request):
    serialier = EventSerializer(data=request.data)
    if serialier.is_valid():
      serialier.save()
      return Response(serialier.data, status=status.HTTP_201_CREATED)
    return Response(serialier.errors, status=status.HTTP_400_BAD_REQUEST)
  
class EventDetailView(APIView):
  authentication_classes = [JWTAuthentication]
 
  def get_permissions(self):
    if self.request.method != 'GET':
      return [IsAuthenticated(), IsAdminOrSuperUser()]
    return [AllowAny()]
  
  def get_object(self, pk):
    try:
      event = Event.objects.get(pk=pk)
      self.check_object_permissions(self.request, event)
      return event
    except Event.DoesNotExist:
      raise Http404
  
  def get(self, request, pk):
    event = self.get_object(pk)
    serializer = EventSerializer(event)
    return Response(serializer.data)
  
  def put(self, request, pk):
    event = self.get_object(pk)
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    event = self.get_object(pk)
    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
