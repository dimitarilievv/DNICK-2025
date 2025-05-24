from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    TYPES=[
        ("on","Online"),
        ("of","Offline"),
    ]
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    date_start=models.DateField()
    date_end=models.DateField()
    image=models.ImageField(upload_to="course-photos/",null=True,blank=True)
    type=models.CharField(max_length=2,choices=TYPES)
    creator=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return f"{self.name} - {self.description}"

class Lecturer(models.Model):
    TYPES = [
        ("p", "Professor"),
        ("a", "Assistant"),
        ("d","Demonstrator")
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100,null=True,blank=True)
    academic_title = models.CharField(max_length=1,choices=TYPES,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    phone=models.IntegerField(default=0)
    country = models.CharField(max_length=100,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return f"{self.name} - {self.surname}"

class CourseLecturer(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL,related_name="courses",null=True)
    def __str__(self):
        return f"{self.course} - {self.lecturer}"


