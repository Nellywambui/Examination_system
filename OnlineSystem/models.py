from django.db import models
from django import forms


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Registration(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name


class Students(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    date_of_birth = models.IntegerField()

    def __str__(self):
        return self.first_name

