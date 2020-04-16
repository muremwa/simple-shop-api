from rest_framework import serializers
from django.contrib.auth.models import User, Permission

from .models import ProductCategory, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = ProductCategory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username', None),
            email=validated_data.get('email', None)
        )
        user.set_password(validated_data.get('password', None))
        user.save()

        # give user permission to add movies
        posting_movies_permission = Permission.objects.get(name='Can add movie')
        user.user_permissions.add(posting_movies_permission)
        return user
