from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db import transaction
from decimal import Decimal
from django.shortcuts import render, redirect

from .models import Sales, SalesDetail
from .forms import SalesForm, SalesDetailFormSet

# Tasa de impuesto constante 
TAX_RATE = Decimal('0.19') 
# Número de lugares decimales
DECIMAL_PLACES = 2

# --- LÓGICA DE NEGOCIO REUTILIZABLE ---

def calculate_sale_totals(sale_instance, details_formset_data):
    total_sale_subtotal_before_tax = Decimal('0.00')
    total_sale_discount_amount = Decimal('0.00')

    for form in details_formset_data:
        if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
            quantity = form.cleaned_data.get('quantity', Decimal('0.00'))
            unit_price = form.cleaned_data.get('unit_price', Decimal('0.00'))
            discount_rate = form.cleaned_data.get('discount', Decimal('0.00')) 

            line_gross_price = quantity * unit_price
            line_discount = line_gross_price * (discount_rate / 100)
            final_line_subtotal = line_gross_price - line_discount
            
            form.instance.subtotal = final_line_subtotal.quantize(Decimal(f'0.{"0"*DECIMAL_PLACES}'))
            
            total_sale_subtotal_before_tax += final_line_subtotal
            total_sale_discount_amount += line_discount

    tax_amount = total_sale_subtotal_before_tax * TAX_RATE
    final_total = total_sale_subtotal_before_tax + tax_amount

    sale_instance.subtotal = total_sale_subtotal_before_tax.quantize(Decimal(f'0.{"0"*DECIMAL_PLACES}'))
    sale_instance.tax = tax_amount.quantize(Decimal(f'0.{"0"*DECIMAL_PLACES}'))
    sale_instance.discount = total_sale_discount_amount.quantize(Decimal(f'0.{"0"*DECIMAL_PLACES}'))
    sale_instance.total = final_total.quantize(Decimal(f'0.{"0"*DECIMAL_PLACES}'))

# --- VISTAS CBV ---

class SalesListView(ListView):
    model = Sales
    template_name = 'sales/sales_list.html'
    context_object_name = 'sales'
    ordering = ['-sale_date']

class SalesDetailView(DetailView):
    model = Sales
    template_name = 'sales/sales_detail.html'
    context_object_name = 'sale'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sale_details'] = self.object.details.all()
        return context

class SalesDeleteView(DeleteView):
    model = Sales
    template_name = 'sales/sales_confirm_delete.html'
    success_url = reverse_lazy('sales-list')

# Mixin para centralizar la lógica de Formset y Totales
class SalesFormsetMixin:
    """Provee la lógica para manejar SalesDetailFormSet y calcular totales."""
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.object if hasattr(self, 'object') else None
        
        if self.request.POST:
            context['details'] = SalesDetailFormSet(self.request.POST, instance=instance)
        else:
            context['details'] = SalesDetailFormSet(instance=instance)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        details_formset = context['details']
        if details_formset.is_valid():
            with transaction.atomic():
                calculate_sale_totals(form.instance, details_formset)
                self.object = form.save()
                details_formset.instance = self.object
                details_formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


# Vista para crear una nueva venta (UTILIZA MIXIN)
class SalesCreateView(SalesFormsetMixin, CreateView):
    model = Sales
    form_class = SalesForm
    template_name = 'sales/sales_form.html'
    success_url = reverse_lazy('sales-list')


# Vista para actualizar una venta existente (UTILIZA MIXIN)
class SalesUpdateView(SalesFormsetMixin, UpdateView):
    model = Sales
    form_class = SalesForm
    template_name = 'sales/sales_form.html' 
    success_url = reverse_lazy('sales-list')
    
