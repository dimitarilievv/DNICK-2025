from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    web_site=models.URLField()
    country = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} - {self.country}"

class Car(models.Model):
    type = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    max_speed=models.IntegerField()
    color=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.type} - {self.manufacturer}"

class ServicePlace(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    can_oldtimer = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} - {self.year_founded}"


class Service(models.Model):
    code=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField()
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to="services/",null=True,blank=True)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    service_place=models.ForeignKey(ServicePlace,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.code} - {self.date}"

class ServicePlaceManufacturer(models.Model):
    service_place = models.ForeignKey(ServicePlace, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.service_place} - {self.manufacturer}"
