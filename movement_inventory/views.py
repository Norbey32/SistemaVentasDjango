from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import MovementInventory
from .forms import MovementInventoryForm

# Vistas CRUD para MovementInventory
class MovementInventoryListView(ListView):
    model = MovementInventory
    template_name = 'movement_inventory/movement_inventory_list.html'
    context_object_name = 'movements'

# Crear un nuevo movimiento de inventario
class MovementInventoryCreateView(CreateView):
    model = MovementInventory
    form_class = MovementInventoryForm
    template_name = 'movement_inventory/movement_inventory_form.html'
    success_url = reverse_lazy('movement-inventory-list')

# Actualizar un movimiento de inventario
class MovementInventoryUpdateView(UpdateView):
    model = MovementInventory
    form_class = MovementInventoryForm
    template_name = 'movement_inventory/movement_inventory_form.html'
    success_url = reverse_lazy('movement-inventory-list')

# Eliminar un movimiento de inventario
class MovementInventoryDeleteView(DeleteView):
    model = MovementInventory
    template_name = 'movement_inventory/movement_inventory_confirm_delete.html'
    success_url = reverse_lazy('movement-inventory-list')