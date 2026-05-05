from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Studio, StudioManager
from .serializers import StudioSerializer, StudioManagerSerializer
from django.http import Http404
 
# Create your views here.
class StudioListCreateView(APIView):
    def get(self, request):
        studios = Studio.objects.all().order_by('name')[:10]
        serializer = StudioSerializer(studios, many=True)
        return Response({'studios': serializer.data})
 
    def post(self, request):
        serializer = StudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class StudioDetailView(APIView):
    def get_object(self, pk):
        try:
            studio = Studio.objects.get(pk=pk)
            self.check_object_permissions(self.request, studio)
            return studio
        except Studio.DoesNotExist:
            raise Http404
 
    def get(self, request, pk):
        studio = self.get_object(pk)
        serializer = StudioSerializer(studio)
        return Response(serializer.data)
 
    def put(self, request, pk):
        studio = self.get_object(pk)
        serializer = StudioSerializer(studio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        studio = self.get_object(pk)
        studio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
class StudioManagerListCreateView(APIView):
    def get(self, request):
        studio_managers = StudioManager.objects.select_related('user', 'studio').all().order_by('user__username')[:10]
        serializer = StudioManagerSerializer(studio_managers, many=True)
        return Response({'studio-managers': serializer.data})
 
    def post(self, request):
        serializer = StudioManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class StudioManagerDetailView(APIView):
    def get_object(self, pk):
        try:
            studio_manager = StudioManager.objects.get(pk=pk)
            self.check_object_permissions(self.request, studio_manager)
            return studio_manager
        except StudioManager.DoesNotExist:
            raise Http404
 
    def get(self, request, pk):
        studio_manager = self.get_object(pk)
        serializer = StudioManagerSerializer(studio_manager)
        return Response(serializer.data)
 
    def put(self, request, pk):
        studio_manager = self.get_object(pk)
        serializer = StudioManagerSerializer(studio_manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        studio_manager = self.get_object(pk)
        studio_manager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)