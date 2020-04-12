from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    established_at = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
