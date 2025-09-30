from django.contrib import admin
from .models import MovementInventory

class MovementInventoryAdmin(admin.ModelAdmin):
    model = MovementInventory
    list_display = ('product', 'movement_type', 'quantity')
    search_fields = ('product__name',)

admin.site.register(MovementInventory, MovementInventoryAdmin)
