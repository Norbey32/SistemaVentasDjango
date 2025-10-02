from django.urls import path
from .views import SalesListView, SalesCreateView, SalesUpdateView, SalesDeleteView, SalesDetailView

urlpatterns = [
    path('', SalesListView.as_view(), name='sales-list'),
    path('crear-venta/', SalesCreateView.as_view(), name='sales-create'),
    path('venta/<int:pk>/', SalesDetailView.as_view(), name='sales-detail'),  # NUEVA
    path('actualizar-venta/<int:pk>/', SalesUpdateView.as_view(), name='sales-update'),
    path('eliminar-venta/<int:pk>/', SalesDeleteView.as_view(), name='sales-delete'),
]