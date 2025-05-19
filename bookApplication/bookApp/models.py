from sre_parse import CATEGORIES

from django.db import models

# Create your models here.
class RecordLabel(models.Model):
    name=models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} - {self.country}"


class Book(models.Model):
    COVER_TYPES = [
        ("S", "Soft"),
        ("H", "Hard")
    ]
    CATEGORY_TYPES = [
        ("R", "Romance"),
        ("T", "Thriller"),
        ("B","Biography"),
        ("C", "Classics"),
        ("D", "Drama"),
        ("H", "History")
    ]

    title=models.CharField(max_length=100)
    photo = models.ImageField(upload_to="book_photos/", null=True, blank=True)
    isbn = models.CharField(max_length=100)
    year_publishing = models.IntegerField()
    record_label =models.ForeignKey(RecordLabel, on_delete=models.CASCADE)
    num_pages = models.IntegerField()
    dimensions = models.CharField(max_length=100)
    cover_type = models.CharField(max_length=1, choices=COVER_TYPES)
    category = models.CharField(max_length=1, choices=CATEGORY_TYPES)
    price=models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.record_label.name}"



