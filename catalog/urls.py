from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    ProductViewSet,
    ProductImageViewSet,
    ProductCharacteristicViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'images', ProductImageViewSet)
router.register(r'characteristics', ProductCharacteristicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
