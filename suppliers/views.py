from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Suppliers
from .forms import SuppliersForm # Asegúrate de crear este formulario

# Vista para listar todos los proveedores.
class SuppliersListView(ListView):
    model = Suppliers
    template_name = 'suppliers/suppliers_list.html'
    context_object_name = 'suppliers'

# Vista para crear un nuevo proveedor.
class SuppliersCreateView(CreateView):
    model = Suppliers
    form_class = SuppliersForm
    template_name = 'suppliers/suppliers_form.html'
    success_url = reverse_lazy('suppliers-list') # Redirige a la lista de proveedores

# Vista para actualizar un proveedor existente.
class SuppliersUpdateView(UpdateView):
    model = Suppliers
    form_class = SuppliersForm
    template_name = 'suppliers/suppliers_form.html'
    success_url = reverse_lazy('suppliers-list')

# Vista para eliminar un proveedor.
class SuppliersDeleteView(DeleteView):
    model = Suppliers
    template_name = 'suppliers/suppliers_confirm_delete.html'
    success_url = reverse_lazy('suppliers-list')