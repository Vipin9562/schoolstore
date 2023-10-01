from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    last = models.CharField(max_length=50)

    def __str__(self):
        return self.name
