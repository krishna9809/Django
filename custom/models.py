from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

class Product(models.Model):
    product_no = models.IntegerField()
    Desc = models.TextField()



