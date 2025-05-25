from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Reservation(models.Model):
    code = models.CharField(max_length=100)
    date_start=models.DateField()
    date_end=models.DateField()
    room = models.ForeignKey('Room',null=True,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='reservations_photos/',null=True,blank=True)
    is_confirmed=models.BooleanField()
    employee=models.ForeignKey('Employee',null=True,blank=True,on_delete=models.CASCADE,limit_choices_to={"type":"r"})
    def __str__(self):
        return f"{self.code}-{self.user}"

class Employee(models.Model):
    CHOICES=[
        ("h","hygienist"),
        ("r","receptionist"),
        ("m","manager")
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    year=models.IntegerField()
    type=models.CharField(max_length=1,choices=CHOICES)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} {self.surname}"

class Room(models.Model):
    number=models.IntegerField()
    num_beds=models.IntegerField()
    has_terrace=models.BooleanField()
    is_cleaned=models.BooleanField()
    def __str__(self):
        return f"{self.number} {self.num_beds}"

class RoomEmployee(models.Model):
    room=models.ForeignKey('Room',null=True,blank=True,on_delete=models.CASCADE)
    # за секоја соба се доделуваат вработени во хотелот - хигиеничари кои треба да ја исчистат so limit
    employee=models.ForeignKey('Employee',null=True,blank=True,on_delete=models.CASCADE,limit_choices_to={"type":"h"})
    def __str__(self):
        return f"{self.room} {self.employee}"