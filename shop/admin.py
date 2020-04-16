from django.contrib import admin

from .models import ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['name', 'description']})
    ]
