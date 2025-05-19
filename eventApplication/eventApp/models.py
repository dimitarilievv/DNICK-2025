from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year_founded = models.IntegerField(null=False, default=2000)
    events_attended = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name} - {self.country}"

class Event(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField(null=True, blank=True)
    poster=models.ImageField(upload_to="posters/", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_closed=models.BooleanField()

    def __str__(self):
        return f"{self.name} - {self.datetime}"

class EventBand(models.Model):
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    band=models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event} {self.band}"


