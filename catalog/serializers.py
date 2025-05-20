from rest_framework import serializers
from .models import Category, Product, ProductImage, Specification

class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ['id', 'key', 'value', 'order']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'order']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    specifications = SpecificationSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'slug', 'image', 'popularity', 'reliability_text', 'special_notes', 'images', 'specifications']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'order']
