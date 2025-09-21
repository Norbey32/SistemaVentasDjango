from django.urls import path
from .views import (
    MovementInventoryListView,
    MovementInventoryCreateView,
    MovementInventoryUpdateView,
    MovementInventoryDeleteView,
)

urlpatterns = [
    path('', MovementInventoryListView.as_view(), name='movement-inventory-list'),
    path('crear-movimiento/', MovementInventoryCreateView.as_view(), name='movement-inventory-create'),
    path('actualizar-movimiento/<int:pk>/', MovementInventoryUpdateView.as_view(), name='movement-inventory-update'),
    path('eliminar-movimiento/<int:pk>/', MovementInventoryDeleteView.as_view(), name='movement-inventory-delete'),
]