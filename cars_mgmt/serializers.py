from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year_of_production', 'fuel_type', 'mileage', 'registration_number']
