# sales/urls.py

from django.urls import path
from .views import (
    SalesListView,
    SalesCreateView,
    SalesUpdateView,
    SalesDeleteView,
    SalesDetailView, 
)

urlpatterns = [
    path('', SalesListView.as_view(), name='sales-detail-list'),
    path('crear-detalle-venta/', SalesCreateView.as_view(), name='salesdetail-create'),
    path('venta/<int:pk>/', SalesDetailView.as_view(), name='sales-detail-detail'),
    path('actualizar-detalle-venta/<int:pk>/', SalesUpdateView.as_view(), name='sales-detail-update'),
    path('eliminar-detalle-venta/<int:pk>/', SalesDeleteView.as_view(), name='sales-detail-delete'),
]