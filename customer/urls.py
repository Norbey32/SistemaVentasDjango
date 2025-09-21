from django.urls import path
from .views import (
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
)

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('crear-cliente/', CustomerCreateView.as_view(), name='customer-create'),
    path('actualizar-cliente/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('eliminar-cliente/<int:pk>/', CustomerDeleteView.as_view(), name='customer-delete'),
]