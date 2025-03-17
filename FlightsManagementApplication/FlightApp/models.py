from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Pilot(models.Model):
    RANK_CHOICES=[
        ('J','Junior'),
        ('I','Intermediate'),
        ('S','Senior'),
    ]
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    total_flight_hours=models.DecimalField(max_digits=5,decimal_places=2)
    rank=models.CharField(max_length=100,choices=RANK_CHOICES)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Balloon(models.Model):
    TYPE_CHOICES = [
        ("S", "Small Balloon"),
        ("M", "Medium Balloon"),
        ("L", "Large Balloon"),
    ]
    type=models.CharField(max_length=100,choices=TYPE_CHOICES)
    name=models.CharField(max_length=100)
    manufacturer=models.CharField(max_length=100)
    max_passengers=models.IntegerField()
    def __str__(self):
        return f"{self.name} {self.manufacturer}"

class Airline(models.Model):
    name=models.CharField(max_length=100)
    year_founded=models.IntegerField()
    outside_Europe=models.BooleanField()
    def __str__(self):
        return f"{self.name} {self.year_founded}"

class AirlinePilot(models.Model):
    airline=models.ForeignKey(Airline,on_delete=models.CASCADE)
    pilot=models.ForeignKey(Pilot,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.airline} {self.pilot}"

class Flight(models.Model):
    code=models.CharField(max_length=100,unique=True)
    take_off_airport=models.CharField(max_length=100)
    landing_airport=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="flight_photos/",null=True,blank=True)
    date=models.DateField()
    balloon=models.ForeignKey(Balloon,on_delete=models.CASCADE)
    pilot=models.ForeignKey(Pilot,on_delete=models.CASCADE)
    airline=models.ForeignKey(Airline,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.take_off_airport} {self.landing_airport}"


