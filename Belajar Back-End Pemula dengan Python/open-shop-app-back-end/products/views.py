from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from products.serializers import ProductSerializer
from .models import Product
from django.http import Http404

class ProductList(APIView):
  def post(self, request):
    product = ProductSerializer(data=request.data, context={'request': request})
    if product.is_valid(raise_exception=True):
      product.save()
      return Response(product.data, status=status.HTTP_201_CREATED)
    return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def get(self, request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response({"products": serializer.data}, status=status.HTTP_200_OK)

class ProductDetail(APIView):
  def get_object(self, pk):
    try:
      return Product.objects.get(pk=pk)
    except Product.DoesNotExist:
      raise Http404
  
  def get(self, request, pk):
    product = self.get_object(pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)