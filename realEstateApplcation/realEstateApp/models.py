from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RealEstate(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    image = models.ImageField(upload_to='real_estates_photos/', null=True, blank=True)
    is_reserved = models.BooleanField()
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}-{self.area}"


class Agent(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.IntegerField()
    linkedin_link = models.URLField()
    number_sales = models.IntegerField()
    email = models.EmailField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"{self.name}-{self.surname}"


class RealEstateAgent(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.real_estate}-{self.agent}"


class Characteristic(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.price}"


class RealEstateCharacteristic(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.real_estate}-{self.characteristic}"
