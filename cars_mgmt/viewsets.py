from rest_framework import viewsets
from . import models
from . import serializers


class CarsViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
