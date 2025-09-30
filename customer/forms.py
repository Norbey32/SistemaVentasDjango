from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    """
    Formulario para la creación y edición de clientes (Customer).
    Aplica clases de Tailwind CSS a todos los campos para la estética, 
    siguiendo el esquema de color azul del formulario de categoría.
    """
    class Meta:
        model = Customer
        # Usamos '__all__' para incluir todos los campos del modelo Customer
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Clase base de Tailwind para dar borde y estilo a todos los campos.
        # NOTA: Usamos focus:ring-blue-500 para igualar el CategoryForm.
        tailwind_class = 'w-full p-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150'

        # Iteramos sobre todos los campos para aplicar la clase y atributos
        for name, field in self.fields.items():
            # El atributo 'attrs' se usa para añadir atributos HTML al widget
            
            if isinstance(field.widget, forms.Textarea):
                # Para Textarea, establecemos un número de filas predeterminado
                field.widget.attrs['rows'] = 4
            
            # Aplicamos la clase Tailwind a todos los widgets
            field.widget.attrs['class'] = tailwind_class
            
            # Mejoramos el placeholder usando el nombre del campo
            if 'placeholder' not in field.widget.attrs:
                # Utilizamos field.label para generar un placeholder útil
                field.widget.attrs['placeholder'] = f'Introduce el valor para {field.label}'
