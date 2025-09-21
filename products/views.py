# products/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Products # Importa tu modelo
from .forms import ProductForm # Crea este formulario

# Vistas CRUD para Products
class ProductListView(ListView):
    model = Products
    template_name = 'products/product_list.html'
    context_object_name = 'products'

# Vista para crear un nuevo producto.
class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product-list')

# Vista para actualizar un producto existente.
class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product-list')

# Vista para eliminar un producto
class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')