from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Sales, SalesDetail
from .forms import SalesForm, SalesDetailFormSet

# Vista para listar todas las ventas
class SalesListView(ListView):
    model = Sales
    template_name = 'sales/sales_list.html'
    context_object_name = 'sales'

# Vista para crear una nueva venta CON detalles
class SalesCreateView(CreateView):
    model = Sales
    form_class = SalesForm
    template_name = 'sales/sales_form.html'
    success_url = reverse_lazy('sales-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['details'] = SalesDetailFormSet(self.request.POST)
        else:
            context['details'] = SalesDetailFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        details = context['details']
        if details.is_valid():
            self.object = form.save()
            details.instance = self.object
            details.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

# Vista para actualizar una venta existente CON detalles
class SalesUpdateView(UpdateView):
    model = Sales
    form_class = SalesForm
    template_name = 'sales/sales_form.html'
    success_url = reverse_lazy('sales-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['details'] = SalesDetailFormSet(self.request.POST, instance=self.object)
        else:
            context['details'] = SalesDetailFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        details = context['details']
        if details.is_valid():
            self.object = form.save()
            details.instance = self.object
            details.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

# Vista para ver el detalle completo de una venta
class SalesDetailView(DetailView):
    model = Sales
    template_name = 'sales/sales_detail.html'
    context_object_name = 'sale'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            # Intenta obtener los detalles, si falla muestra lista vacía
            context['sale_details'] = self.object.details.all()
        except:
            context['sale_details'] = []
        return context

# Vista para eliminar una venta
class SalesDeleteView(DeleteView):
    model = Sales
    template_name = 'sales/sales_confirm_delete.html'
    success_url = reverse_lazy('sales-list')