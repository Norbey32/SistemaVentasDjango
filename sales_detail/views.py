from django.views.generic import DetailView
from .models import SaleDetail

# Vista para mostrar los detalles de un registro de venta.
class SalesDetailView(DetailView):
    model = SaleDetail
    template_name = 'sales/sales_detail.html'
    context_object_name = 'sales_detail'