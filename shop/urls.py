from django.urls import path

from . import views


urlpatterns = [
    # shop/product-category/
    path('product-category/', views.ProductCategoryIndex.as_view(), name='product-category-index'),

    # shop/product-category/home-appliances/
    path(
        'product-category/<str:product_category_slug>/',
        views.ProductCategoryDetail.as_view(),
        name='product-category-detail'
    ),

    # shop/product/
    path('product/', views.ProductIndex.as_view(), name='products-index'),

    # shop/product/product-slug/
    path('product/<str:product_slug>/', views.ProductDetail.as_view(), name='product-detail'),
]
