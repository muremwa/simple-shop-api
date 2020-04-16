from rest_framework import generics

from .models import ProductCategory, Product
from .serializers import ProductCategorySerializer, ProductSerializer, UserSerializer


class ProductCategoryIndex(generics.ListCreateAPIView):
    """Fetch all product categories or create a new one"""
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """fetch a single product category using the slug field or update a product category or delete a product category"""
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    lookup_url_kwarg = 'product_category_slug'
    lookup_field = 'slug'


class ProductIndex(generics.ListCreateAPIView):
    """Fetches all products or creates a new one"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """Fetch a particular product using the slug or Update a particular product or delete a product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_slug'
    lookup_field = 'slug'


class CreateUser(generics.CreateAPIView):
    """Create a user with permission to add movies"""
    serializer_class = UserSerializer
