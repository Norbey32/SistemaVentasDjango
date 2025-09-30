from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Categories 
from .forms import CategoryForm 

# Vistas CRUD para Categories
class CategoryListView(ListView):
    model = Categories
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

# Vista para crear una nueva categoría.
class CategoryCreateView(CreateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category-list') 

# Vista para actualizar una categoría existente.
class CategoryUpdateView(UpdateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category-list')

# Vista para eliminar una categoría
class CategoryDeleteView(DeleteView):
    model = Categories
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')