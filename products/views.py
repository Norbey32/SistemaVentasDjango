from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product 
from .forms import ProductForm 

# Vistas CRUD para Products
class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'

# Vista para crear un nuevo producto.
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/products_form.html'
    success_url = reverse_lazy('product-list')

# Vista para actualizar un producto existente.
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product-list')

# Vista para eliminar un producto
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')