from django.urls import path
from .views import CategoryListView, CategoryDetailView, ProductDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),  # список всех категорий
    path('catalog/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('catalog/<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product-detail'),
]
