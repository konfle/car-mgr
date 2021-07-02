from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    year_of_production = models.SmallIntegerField(default=2000, blank=True)
    fuel_type = models.CharField(max_length=10, blank=True, null=True)
    mileage = models.DecimalField(default=0, max_digits=8, decimal_places=1, blank=True, null=True)
    registration_number = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.show_car()

    def show_car(self):
        return "{} - {} - {}".format(self.brand, self.model, self.year_of_production)
