from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Sales
from .forms import SalesForm

# Vista para listar todos los registros de ventas.
class SalesListView(ListView):
    model = Sales
    template_name = 'sales/sales_list.html'
    context_object_name = 'sales'

# Vista para crear un nuevo registro de venta.
class SalesCreateView(CreateView):
    model = Sales
    form_class = SalesForm
    template_name = 'sales/sales_form.html'
    success_url = reverse_lazy('sales-list') # Redirige a la lista de ventas

# Vista para actualizar un registro de venta existente.
class SalesUpdateView(UpdateView):
    model = Sales
    form_class = SalesForm
    template_name = 'sales/sales_form.html'
    success_url = reverse_lazy('sales-list')

# Vista para eliminar un registro de venta.
class SalesDeleteView(DeleteView):
    model = Sales
    template_name = 'sales/sales_confirm_delete.html'
    success_url = reverse_lazy('sales-list')