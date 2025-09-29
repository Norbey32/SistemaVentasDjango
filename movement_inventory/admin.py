from django.contrib import admin
from .models import MovementInventory

class MovementInventoryAdmin(admin.ModelAdmin):
    model = MovementInventory
    list_display = ('product', 'movement_type', 'quantity', 'movement_date', 'created_at')
    search_fields = ('product__name', 'movement_type')

admin.site.register(MovementInventory, MovementInventoryAdmin)
