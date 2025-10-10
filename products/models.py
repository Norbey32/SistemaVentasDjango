from django.db import models
from categories.models import Categories
from suppliers.models import Suppliers


# Definición del ENUM para el Estado del Producto
class EstadoProducto(models.TextChoices):
    ACTIVO = 'ACT', 'Activo (Disponible)'
    INACTIVO = 'INA', 'Inactivo (No disponible)'
    AGOTADO = 'AGO', 'Agotado (Sin stock)'
    DESCONTINUADO = 'DSC', 'Descontinuado'


class Product(models.Model):
    code = models.CharField(max_length=50, verbose_name="Código")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    description = models.TextField(max_length=500, verbose_name="Descripción")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")
    current_stock = models.PositiveIntegerField(verbose_name="Stock Actual")
    minimum_stock = models.PositiveIntegerField(verbose_name="Stock Mínimo")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Categoría")
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, verbose_name="Proveedor")
    product_state = models.CharField(
        max_length=3,
        choices=EstadoProducto.choices,
        default=EstadoProducto.ACTIVO,
        verbose_name="Estado del Producto"
    )


    def __str__(self):
        return f"{self.name} ({self.get_product_state_display()})"
