from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Movie
from .serializers import MovieSerializer, MoviePosterSerializer
from core.permissions import IsAdminOrSuperUser
import tempfile
import os
from minio import Minio
from rest_framework.parsers import MultiPartParser, FormParser
 
# Create your views here.
class MovieListCreateView(APIView):

    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminOrSuperUser()]
        return [IsAuthenticated()]

    def get(self, request):
        movies = Movie.objects.all().order_by('name')[:10]
        serializer = MovieSerializer(movies, many=True)
        return Response({'movies': serializer.data})
 
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class MovieDetailView(APIView):

    authentication_classes = [JWTAuthentication]
 
    def get_permissions(self):
        if self.request.method != 'GET':
            return [IsAuthenticated(), IsAdminOrSuperUser()]
        return [IsAuthenticated()]
    
    def get_object(self, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            self.check_object_permissions(self.request, movie)
            return movie
        except Movie.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
 
    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def get_minio_client():
    return Minio(
        endpoint=os.getenv('MINIO_ENDPOINT_URL'),
        access_key=os.getenv('MINIO_ACCESS_KEY'),
        secret_key=os.getenv('MINIO_SECRET_KEY'),
        secure=False
    )
 
bucket_name = os.getenv('MINIO_BUCKET_NAME')

class MoviePosterView(APIView):
    authentication_classes = [JWTAuthentication]
    parser_classes = [MultiPartParser, FormParser]
 
    def get_permissions(self):
        return [IsAuthenticated(), IsAdminOrSuperUser()]
 
    def post(self, request):
        serializer = MoviePosterSerializer(data=request.data)
        file = request.data.get('image')
 
        if serializer.is_valid():
            serializer.save()
 
            # Simpan file sementara sebelum upload ke Minio
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in file.chunks():
                    temp_file.write(chunk)
                temp_file_path = temp_file.name
 
            try:
                object_name = f"{serializer.instance.image.name}"
                client = get_minio_client()
                client.fput_object(bucket_name, object_name, temp_file_path, content_type=file.content_type)
            except Exception as e:
                return Response(
                    {"error": f"Upload to Minio failed: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            finally:
                os.remove(temp_file_path)
 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MoviePosterDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
 
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        images = movie.movieposter_set.all()
 
        serialized_images = []
        for image in images:
            client = get_minio_client()
            presigned_url = client.presigned_get_object(
                bucket_name,
                image.image.name,
                response_headers={"response-content-type": "image/jpeg"}
            )
            serialized_images.append({"id": image.id, "url": presigned_url})
 
        return Response(serialized_images)