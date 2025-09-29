from django.contrib import admin
from .models import Sales

class SalesAdmin(admin.ModelAdmin):
    model = Sales
    list_display = ('id', 'product', 'quantity', 'sale_date', 'total')
    search_fields = ('product_name')

admin.site.register(Sales, SalesAdmin)
