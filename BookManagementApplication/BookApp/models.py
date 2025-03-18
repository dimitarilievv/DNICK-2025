from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    def __str__(self):
        return f"{self.name} {self.description}"

class Translator(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    def __str__(self):
        return f"{self.name} {self.nationality}"

class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    def __str__(self):
        return f"{self.name} {self.nationality}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    release_date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    num_pages=models.IntegerField()
    cover_photo=models.ImageField(upload_to='covers/',null=True,blank=True)
    is_available=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title} {self.author}"

class BookGenres(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)

class BookTranslator(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    translator=models.ForeignKey(Translator,on_delete=models.CASCADE)

class BookAuthor(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.user} {self.rating} {self.comment}"
