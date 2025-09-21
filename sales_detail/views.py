from django.views.generic import DetailView
from .models import Sales

# Vista para mostrar los detalles de un registro de venta.
class SalesDetailView(DetailView):
    model = Sales
    template_name = 'sales/sales_detail.html'
    context_object_name = 'sale'