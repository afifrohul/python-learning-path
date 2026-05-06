from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404
from .models import Ticket
from .serializers import TicketSerializer
from core.permissions import IsAdminOrSuperUser

# Create your views here.
class TicketListCreateView(APIView):
  authentication_classes =[JWTAuthentication]

  def get_permissions(self):
    if self.request.method == 'POST':
      return [IsAuthenticated(), IsAdminOrSuperUser()]
    return [IsAuthenticated()]
  
  def get(self, request):
    tickets = Ticket.objects.all().order_by('name')[:10]
    serializer = TicketSerializer(tickets, many=True)
    return Response({'tickets': serializer.data})
  
  def post(self, request):
    serialier = TicketSerializer(data=request.data)
    if serialier.is_valid():
      serialier.save()
      return Response(serialier.data, status=status.HTTP_201_CREATED)
    return Response(serialier.errors, status=status.HTTP_400_BAD_REQUEST)
  
class TicketDetailView(APIView):
  authentication_classes = [JWTAuthentication]
 
  def get_permissions(self):
    if self.request.method != 'GET':
      return [IsAuthenticated(), IsAdminOrSuperUser()]
    return [AllowAny()]
  
  def get_object(self, pk):
    try:
      ticket = Ticket.objects.get(pk=pk)
      self.check_object_permissions(self.request, ticket)
      return ticket
    except Ticket.DoesNotExist:
      raise Http404
  
  def get(self, request, pk):
    ticket = self.get_object(pk)
    serializer = TicketSerializer(ticket)
    return Response(serializer.data)
  
  def put(self, request, pk):
    ticket = self.get_object(pk)
    serializer = TicketSerializer(ticket, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    ticket = self.get_object(pk)
    ticket.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)