from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tailwind_class = 'w-full p-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150'
        for name, field in self.fields.items():
            
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['rows'] = 4
            field.widget.attrs['class'] = tailwind_class

            if 'placeholder' not in field.widget.attrs:
                field.widget.attrs['placeholder'] = f'Introduce el valor para {field.label}'
