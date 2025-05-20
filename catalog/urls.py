from django.urls import path
from .views import CategoryListView, CategoryDetailView, ProductDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),  # /api/catalog/
    path('<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),  # /api/catalog/<slug>/
    path('<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product-detail'),  # /api/catalog/<category>/<product>/
]
