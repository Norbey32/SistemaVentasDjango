from django.db import models
from customer.models import Customer
from employee.models import Employee
from products.models import Product


# Definición del ENUM para el Método de Pago
class MetodoPago(models.TextChoices):
    EFECTIVO = 'EFE', 'Efectivo'
    TARJETA_CREDITO = 'TCR', 'Tarjeta de Crédito'
    TARJETA_DEBITO = 'TDE', 'Tarjeta de Débito'
    TRANSFERENCIA = 'TRA', 'Transferencia Bancaria'
    CHEQUE = 'CHQ', 'Cheque'
    PAGO_MOVIL = 'PMO', 'Pago Móvil'
    CRIPTOMONEDA = 'CRP', 'Criptomoneda'


# Definición del ENUM para el Estado de Venta
class EstadoVenta(models.TextChoices):
    COMPLETADA = 'CMP', 'Completada'
    PENDIENTE = 'PEN', 'Pendiente de Pago'
    CANCELADA = 'CAN', 'Cancelada'
    DEVUELTA = 'DEV', 'Devuelta'
    EN_PROCESO = 'PRC', 'En Proceso (Borrador)'


class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name="Cliente")
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name="Empleado")
    sale_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Venta")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")
    tax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Impuesto")
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Descuento")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    payment_method = models.CharField(
        max_length=3,
        choices=MetodoPago.choices,
        default=MetodoPago.EFECTIVO,
        verbose_name="Método de Pago"
    )
    sale_state = models.CharField(
        max_length=3,
        choices=EstadoVenta.choices,
        default=EstadoVenta.PENDIENTE,
        verbose_name="Estado de la Venta"
    )


    def __str__(self):
        return f"Venta # {self.id} ({self.get_sale_state_display()})"

class SalesDetail(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE, related_name='details', verbose_name="Venta")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Producto")
    quantity = models.IntegerField(verbose_name="Cantidad")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Descuento")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")


    def __str__(self):
        return f"Detail #{self.id} - Sale #{self.sale.id}"
