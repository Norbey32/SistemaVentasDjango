from django import forms
from .models import MovementInventory

class MovementInventoryForm(forms.ModelForm):
    class Meta:
        model = MovementInventory
        fields = '__all__'