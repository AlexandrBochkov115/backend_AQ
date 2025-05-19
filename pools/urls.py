from django.urls import path
from .views import PoolListView, PoolDetailView

urlpatterns = [
    path('pools/', PoolListView.as_view(), name='pool-list'),
    path('pools/<slug:slug>/', PoolDetailView.as_view(), name='pool-detail'),
]