from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import views


schema_view = get_swagger_view(title='Simple Shop API')


urlpatterns = [
    path('', schema_view, name='swagger-documentation'),

    # shop/product-category/
    path('product-category/', views.ProductCategoryIndex.as_view(), name='product-category-index'),

    # shop/product-category/home-appliances/
    path(
        'product-category/<str:product_category_slug>/',
        views.ProductCategoryDetail.as_view(),
        name='product-category-detail'
    ),
]
