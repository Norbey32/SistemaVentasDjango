from django import forms
from .models import Products  # Asegúrate de que el nombre del modelo sea 'Products'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'