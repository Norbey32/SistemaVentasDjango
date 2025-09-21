# posts/urls.py

from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('crear-cargo/', PostCreateView.as_view(), name='post-create'),
    path('actualizar-cargo/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('eliminar-cargo/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
]