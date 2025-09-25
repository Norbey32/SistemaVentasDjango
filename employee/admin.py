from django.contrib import admin
from .models import employee


class EmployeeAdmin(admin.ModelAdmin):
    model = employee
    list_display = ('id', 'name', 'last_name', 'email', 'phone_number')
    search_fields = ('name')
