from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Baker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='bakers/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Cake(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.IntegerField()
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="cake_photos/", null=True, blank=True)
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE, null=True, blank=True, related_name='cakes')

    def __str__(self):
        return f"{self.name}"
