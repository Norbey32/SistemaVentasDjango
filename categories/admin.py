from django.contrib import admin
from .models import Categories

class CategoriesAdmin(admin.ModelAdmin):
    model = Categories
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name')

admin.site.register(Categories, CategoriesAdmin)