from rest_framework import generics

from .models import ProductCategory, Product
from .serializers import ProductCategorySerializer, ProductSerializer


class ProductCategoryIndex(generics.ListCreateAPIView):
    """fetches all product categories or creates a new one"""
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    fetches a single product category using the slug field
    update a product category
    delete a product category
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    lookup_url_kwarg = 'product_category_slug'
    lookup_field = 'slug'


class ProductIndex(generics.ListCreateAPIView):
    """Fetches all products or creates a new one"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Fetch a particular product using the slug
    Update a particular product
    delete a product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_slug'
    lookup_field = 'slug'
