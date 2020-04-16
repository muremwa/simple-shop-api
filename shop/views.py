from rest_framework import generics

from .models import ProductCategory
from .serializers import ProductCategorySerializer


class ProductCategoryIndex(generics.ListCreateAPIView):
    """fetches all product categories"""
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    fetches a single product category using the slug field
    update a product category
    delete a product category
    """
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    lookup_url_kwarg = 'product_category_slug'
    lookup_field = 'slug'
