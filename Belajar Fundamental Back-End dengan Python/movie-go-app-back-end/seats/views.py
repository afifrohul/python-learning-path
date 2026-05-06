from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Seat
from .serializers import SeatSerializer
from django.http import Http404
from core.permissions import IsAdminOrSuperUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
 
# Create your views here.
class SeatListCreateView(APIView):

    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminOrSuperUser()]
        return [IsAuthenticated()]

    def get(self, request):
        seats = Seat.objects.all().order_by('seat_number')[:10]
        serializer = SeatSerializer(seats, many=True)
        return Response({'seats': serializer.data})
 
    def post(self, request):
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class SeatDetailView(APIView):

    authentication_classes = [JWTAuthentication]
 
    def get_permissions(self):
        if self.request.method != 'GET':
            return [IsAuthenticated(), IsAdminOrSuperUser()]
        return [IsAuthenticated()]

    def get_object(self, pk):
        try:
            seat = Seat.objects.get(pk=pk)
            self.check_object_permissions(self.request, seat)
            return seat
        except Seat.DoesNotExist:
            raise Http404
 
    def get(self, request, pk):
        seat = self.get_object(pk)
        serializer = SeatSerializer(seat)
        return Response(serializer.data)
 
    def put(self, request, pk):
        seat = self.get_object(pk)
        serializer = SeatSerializer(seat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        seat = self.get_object(pk)
        seat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)