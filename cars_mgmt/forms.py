from django.forms import ModelForm
from .models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year_of_production', 'fuel_type', 'mileage', 'registration_number']
