from django import forms
from django.forms import ModelForm
from .models import Categories

class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150',
                'placeholder': 'Ej. Productos Lácteos'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150',
                'rows': 4,
                'placeholder': 'Una descripción detallada de la categoría.'
            }),
        }
