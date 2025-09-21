# products/urls.py

from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('crear-producto/', ProductCreateView.as_view(), name='product-create'),
    path('actualizar-producto/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('eliminar-producto/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
]