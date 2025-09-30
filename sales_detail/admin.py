from django.contrib import admin
from .models import SaleDetail

class SaleDetailAdmin(admin.ModelAdmin):
    model = SaleDetail
    list_display = ('sale', 'product', 'quantity')
    list_filter = ('sale', 'product')

admin.site.register(SaleDetail, SaleDetailAdmin)
