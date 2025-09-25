from django.contrib import admin
from .models import Sale

class SaleAdmin(admin.ModelAdmin):
    model = Sale
    list_display = ('id', 'product', 'quantity', 'sale_date', 'total')
    search_fields = ('product__name',)

admin.site.register(Sale, SaleAdmin)
