from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ('id', 'name', 'email', 'phone_number', 'created_at')
    search_fields = ('name')
    
admin.site.register(Customer, CustomerAdmin)



