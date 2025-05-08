from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    year_of_establishment = models.CharField(max_length=4)
    number_of_employees = models.IntegerField()
    def __str__(self):
        return f"{self.name} {self.user}"

class Car(models.Model):
    CAR_TYPES = [
        ("SE", "Sedan"),
        ("SY", "SUV"),
        ("HA", "Hatchback"),
        ("CO","Coupe")
    ]
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    chassis_number=models.IntegerField()
    model=models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year_of_production=models.CharField(max_length=4)
    mileage=models.DecimalField(max_digits=10,decimal_places=2)
    car_type = models.CharField(max_length=2, choices=CAR_TYPES)
    photo=models.ImageField(upload_to="car_photos/", null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

