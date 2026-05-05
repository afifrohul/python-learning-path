from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Showtime
from .serializers import ShowtimeSerializer
from django.http import Http404
 
# Create your views here.
class ShowtimeListCreateView(APIView):
    def get(self, request):
        showtimes = Showtime.objects.all().order_by('start_time')[:10]
        serializer = ShowtimeSerializer(showtimes, many=True)
        return Response({'showtimes': serializer.data})
 
    def post(self, request):
        serializer = ShowtimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class ShowtimeDetailView(APIView):
    def get_object(self, pk):
        try:
            showtime = Showtime.objects.get(pk=pk)
            self.check_object_permissions(self.request, showtime)
            return showtime
        except Showtime.DoesNotExist:
            raise Http404
 
    def get(self, request, pk):
        showtime = self.get_object(pk)
        serializer = ShowtimeSerializer(showtime)
        return Response(serializer.data)
 
    def put(self, request, pk):
        showtime = self.get_object(pk)
        serializer = ShowtimeSerializer(showtime, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        showtime = self.get_object(pk)
        showtime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)