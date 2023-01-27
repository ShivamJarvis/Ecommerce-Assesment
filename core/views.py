from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser
from core.models import Product
from django_filters.rest_framework import DjangoFilterBackend
from core import serializers
# Create your views here.

def index(request):
    return render(request,'index.html')

class ProductCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAdminUser]

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_popular']
    
class ProductDetailView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [AllowAny]

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAdminUser]