from django.urls import path
from .views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
)

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('crear-empleado/', EmployeeCreateView.as_view(), name='employee-create'),
    path('actualizar-empleado/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('eliminar-empleado/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
]