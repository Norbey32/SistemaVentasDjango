from django.db import models
from products.models import Product
from employee.models import Employee
from sales.models import Sales


# Modelo para tipo de movimiento
class TipoMovimiento(models.TextChoices):
    ENTRADA = 'ENT', 'Entrada (Compra/Ingreso)'
    SALIDA = 'SAL', 'Salida (Venta/Daño)'
    AJUSTE = 'AJU', 'Ajuste de Inventario'
    TRANSFERENCIA = 'TRA', 'Transferencia entre Almacenes'
    DEVOLUCION = 'DEV', 'Devolución de Cliente'


# Modelo de Inventario con el TipoMovimiento
class MovementInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    movement_type = models.CharField(max_length=3, choices=TipoMovimiento.choices, default=TipoMovimiento.AJUSTE, verbose_name='Tipo de Movimiento')
    quantity = models.IntegerField(verbose_name='Cantidad')
    movement_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Movimiento')
    note = models.TextField(blank=True, null=True, verbose_name='Nota')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Empleado')
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Venta Relacionada')


    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.product.name} - {self.quantity}"
