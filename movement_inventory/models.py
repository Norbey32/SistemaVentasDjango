from django.db import models
from products.models import Products
from employees.models import Employee
from sales.models import Sales

class MovementInventory(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    movement_date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f"{self.movement_type} - {self.product.name} - {self.quantity}"
