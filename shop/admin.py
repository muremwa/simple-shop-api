from django.contrib import admin

from .models import ProductCategory, Product, Movie


admin.site.register(Movie)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['name', 'description']})
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['name', 'description', 'price', 'product_category']})
    ]
    list_display = ['name', 'price', 'product_category']
    list_filter = ['product_category']
