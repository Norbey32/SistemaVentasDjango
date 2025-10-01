# sales/forms.py

from django import forms
from .models import Sales 

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tailwind_class = 'w-full p-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150'
        
        for name, field in self.fields.items():
            field.widget.attrs['class'] = tailwind_class
            
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['rows'] = 4
                
            if 'placeholder' not in field.widget.attrs:
                field.widget.attrs['placeholder'] = f'Introduce el valor para {field.label.lower()}'
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] += ' appearance-none cursor-pointer'