from random import choices

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ContactInfo(models.Model):
    street_name = models.CharField(max_length=100)
    street_number = models.IntegerField()
    phone_number = models.IntegerField()
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.street_name} - {self.street_number}, {self.phone_number},{self.email_address}"


class Market(models.Model):
    name = models.CharField(max_length=100)
    # employees --> onetomany
    # products --> manytomany new table
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    number_market = models.IntegerField()
    date_created = models.DateField()
    # user that added this market
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    working_time_from = models.TimeField()
    working_time_to = models.TimeField()

    def __str__(self):
        return f"{self.name} (work time: {self.working_time_from}-{self.working_time_to})"


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    ssn = models.CharField(max_length=13, unique=True)
    # user that added this employee
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # employee M - 1 market foreign key here
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    salary = models.DecimalField(decimal_places=1, max_digits=50)

    def __str__(self):
        return f"{self.name} - {self.surname}"


class Product(models.Model):
    TYPE_CHOICES = [
        ("F", "Food"),
        ("D", "Drink"),
        ("B", "Bakery"),
        ("C", "Cosmetics"),
        ("H", "Hygiene"),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    is_homemade = models.BooleanField(default=False)
    code = models.CharField(max_length=100, unique=True)

    def ___str__(self):
        #for the keys self.type - for the values get_type_display
        return f"{self.name} - {self.get_type_display()} - {'Homemade' if self.is_homemade else 'Not Homemade'} - {self.code}"


class MarketProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.market.name}"
