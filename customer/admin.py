from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name',)
    
admin.site.register(Customer, CustomerAdmin)



