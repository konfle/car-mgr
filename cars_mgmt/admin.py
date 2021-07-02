from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year_of_production', 'registration_number']
    list_filter = ['brand', 'model', 'year_of_production', 'fuel_type']
    search_fields = ['registration_number']
