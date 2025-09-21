# categories/urls.py

from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('crear-categoria/', CategoryCreateView.as_view(), name='category-create'),
    path('actualizar-categoria/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('eliminar-categoria/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),
]