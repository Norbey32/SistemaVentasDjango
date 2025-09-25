from django.contrib import admin
from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
    list_display = ('name', 'contact_email', 'phone_number', 'address')
    search_fields = ('name',)

admin.site.register(Supplier, SupplierAdmin)
