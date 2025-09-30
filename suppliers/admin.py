from django.contrib import admin
from .models import Suppliers


class SuppliersAdmin(admin.ModelAdmin):
    model = Suppliers
    list_display = ('name', 'contact', 'phone')
    search_fields = ('name',)

admin.site.register(Suppliers, SuppliersAdmin)
