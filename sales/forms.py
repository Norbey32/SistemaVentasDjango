from django import forms
from django.forms import inlineformset_factory
from .models import Sales, SalesDetail 

# Formulario principal para la Venta 
class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['customer', 'employee', 'payment_method', 'sale_state'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tailwind_class = 'w-full p-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150'
        
        for name, field in self.fields.items():
            field.widget.attrs['class'] = tailwind_class
            
            if 'placeholder' not in field.widget.attrs:
                field.widget.attrs['placeholder'] = f'Seleccione o ingrese el valor para {field.label.lower()}'
            
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] += ' appearance-none cursor-pointer bg-white'



class SalesDetailForm(forms.ModelForm):
    class Meta:
        model = SalesDetail
        fields = ['product', 'quantity', 'unit_price', 'discount'] 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tailwind_class = 'w-full p-2 text-sm border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500'
        
        for name, field in self.fields.items():
            field.widget.attrs['class'] = tailwind_class
            field.widget.attrs['placeholder'] = field.label


SalesDetailFormSet = inlineformset_factory(
    Sales,          # Modelo padre
    SalesDetail,    # Modelo hijo
    form=SalesDetailForm,  # Formulario personalizado para el detalle
    extra=1,        # Se recomienda un número bajo de 'extra' (e.g., 1 o 2) para mejor UX
    can_delete=True,  # Permite eliminar filas de detalle
    min_num=1,      # Mínimo de un detalle por venta
    validate_min=True 
)
