from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


# Получение категории по slug + список продуктов в ней
class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        products = category.products.all()
        products_serializer = ProductSerializer(products, many=True, context={'request': request})
        category_serializer = self.get_serializer(category)

        data = category_serializer.data
        data['products'] = products_serializer.data  # добавляем продукты к ответу

        return Response(data)


# Детали продукта по slug категории и slug продукта
class ProductDetailView(APIView):
    def get(self, request, category_slug, product_slug):
        category = get_object_or_404(Category, slug=category_slug)
        product = get_object_or_404(Product, slug=product_slug, category=category)

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer