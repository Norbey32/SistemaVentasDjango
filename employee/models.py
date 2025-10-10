from django.db import models
from post.models import Post


# Definición del ENUM para el Estado del Empleado
class EstadoEmpleado(models.TextChoices):
    ACTIVO = 'ACT', 'Activo'
    INACTIVO = 'INA', 'Inactivo'
    VACACIONES = 'VAC', 'Vacaciones'
    LICENCIA = 'LIC', 'Licencia'
    SUSPENDIDO = 'SUS', 'Suspendido'
    RETIRADO = 'RET', 'Retirado'


class Employee(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    last_name = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='employees', 
        verbose_name="Puesto/Cargo"
    )
    hiring_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Contratación")
    state = models.CharField(
        max_length=3,
        choices=EstadoEmpleado.choices,
        default=EstadoEmpleado.ACTIVO,
        verbose_name="Estado Laboral"
    )


    def __str__(self):
        return f"{self.name} {self.last_name} ({self.get_state_display()})"
