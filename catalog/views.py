from rest_framework import viewsets
from .models import Category, Product, ProductImage, ProductCharacteristic
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductImageSerializer,
    ProductCharacteristicSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductCharacteristicViewSet(viewsets.ModelViewSet):
    queryset = ProductCharacteristic.objects.all()
    serializer_class = ProductCharacteristicSerializer
