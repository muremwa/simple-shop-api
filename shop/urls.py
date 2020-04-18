from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views


schema_view = get_swagger_view(title='Simple Shop Api')


urlpatterns = [
    # shop/
    path('', schema_view, name='documentation'),

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

    # shop/create-user/
    path('create-user/', views.CreateUser.as_view(), name='create-user'),

    # shop/user-token/
    path('user-token/', TokenObtainPairView.as_view(), name='obtain-token'),

    # shop/user-token/refresh/
    path('user-toke/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]
