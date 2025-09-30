from django import forms
from django.forms import ModelForm
from .models import Categories

class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                # Clase para input de texto: ancho completo, padding, borde, redondeo, sombra y foco azul.
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150',
                'placeholder': 'Ej. Productos Lácteos'
            }),
            'description': forms.Textarea(attrs={
                # Clase para textarea: misma clase, pero le añadimos 'rows: 4' para la altura.
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150',
                'rows': 4,
                'placeholder': 'Una descripción detallada de la categoría.'
            }),
        }
