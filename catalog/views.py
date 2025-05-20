from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        products = category.products.all()
        products_serializer = ProductSerializer(products, many=True, context={'request': request})
        category_serializer = self.get_serializer(category)

        data = category_serializer.data
        data['products'] = products_serializer.data
        return Response(data)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'slug'  # По какому полю ищем продукт
    lookup_url_kwarg = 'product_slug'  # Как называется параметр в URL

    def get_object(self):
        # Получаем slug категории и продукта из URL
        category_slug = self.kwargs['category_slug']
        product_slug = self.kwargs['product_slug']

        # Ищем продукт в указанной категории
        return get_object_or_404(
            Product,
            category__slug=category_slug,
            slug=product_slug
        )

    def get_queryset(self):
        """Базовый queryset для проверки прав доступа"""
        category_slug = self.kwargs.get('category_slug')
        category = get_object_or_404(Category, slug=category_slug)
        return Product.objects.filter(category=category)