from django.db import models
from categories.models import Categories
from suppliers.models import Suppliers


class Product(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_stock = models.PositiveIntegerField()
    minimum_stock = models.PositiveIntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)


    def __str__(self):
        return self.name
