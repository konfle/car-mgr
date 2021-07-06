from django.db import models


class Car(models.Model):

    class CarBrands(models.TextChoices):
        ALFA_ROMEO = 'Alfa Romeo'
        AUDI = 'Audi'
        BMW = 'BMW'
        CHEVROLET = 'Chevrolet'
        CHRYSLET = 'Chrysler'
        CITROEN = 'Citroen'
        DACIA = 'Dacia'
        FIAT = 'Fiat'
        FORD = 'Ford'
        HONDA = 'Honda'
        HYUNDAI = 'Hyundai'
        INFINITI = 'Infiniti'
        JAGUAR = 'Jaguar'
        JEEP = 'Jeep'
        KIA = 'Kia'
        LANCIA = 'Lancia'
        LAND_ROVER = 'Land Rover'
        LEXUS = 'Lexus'
        MINI = 'Mini'
        MAZDA = 'Mazda'
        MERCEDES_BENZ = 'Mercedes Benz'
        MITSHUBISHI = 'Mitsubishi'
        NISSAN = 'Nissan'
        OPEL = 'Opel'
        PEUGEOT = 'Peugeot'
        PORSCHE = 'Porsche'
        RENAULT = 'Renault'
        SEAT = 'Seat'
        SAAB = 'Saab'
        SKODA = 'Skoda'
        SSANGYONG = 'Ssangyong'
        SUBARU = 'Subaru'
        SUZUKI = 'Suziki'
        TOYOTA = 'Toyota'
        VOLKSWAGEN = 'Volkswagen'
        VOLVO = 'Volvo'

    brand = models.CharField(max_length=20, blank=True, null=True, choices=CarBrands.choices)
    model = models.CharField(max_length=20, blank=True, null=True)
    year_of_production = models.SmallIntegerField(default=2000, blank=True)

    class CarFuelType(models.TextChoices):
        BENZINE = 'Benzine'
        BIOFUELS = 'Biofuels'
        DIESEL = 'Diesel'
        ELECTRIC = 'Electric'
        HYBRID = 'Hybrid'
        LPG = 'LPG'

    fuel_type = models.CharField(max_length=10, blank=True, null=True, choices=CarFuelType.choices)
    mileage = models.DecimalField(default=0, max_digits=8, decimal_places=1, blank=True, null=True)
    registration_number = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.show_car()

    def show_car(self):
        return "{} - {} - {}".format(self.brand, self.model, self.year_of_production)
