from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

urlpatterns = [
    # shop/
    path('', RedirectView.as_view(url='/shop/')),

    # admin/
    path('admin/', admin.site.urls),

    # shop/*
    path('shop/', include('shop.urls')),

]
