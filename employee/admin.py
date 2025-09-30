from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name',)
