from django.urls import path
from .views import (
    SuppliersListView,
    SuppliersCreateView,
    SuppliersUpdateView,
    SuppliersDeleteView,
)

urlpatterns = [
    path('', SuppliersListView.as_view(), name='suppliers-list'),
    path('crear-proveedor/', SuppliersCreateView.as_view(), name='suppliers-create'),
    path('actualizar-proveedor/<int:pk>/', SuppliersUpdateView.as_view(), name='suppliers-update'),
    path('eliminar-proveedor/<int:pk>/', SuppliersDeleteView.as_view(), name='suppliers-delete'),
]