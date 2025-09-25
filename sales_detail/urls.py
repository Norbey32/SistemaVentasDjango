from django.urls import path
from .views import SalesDetailView

urlpatterns = [
    path('venta/<int:pk>/', SalesDetailView.as_view(), name='sales-detail-detail'),
]