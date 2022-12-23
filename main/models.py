from django.db import models
from datetime import date


class aboutAdmin(models.Model):
    def calculate_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    name = models.CharField(max_length=30)
    description = models.TextField(default="")
    birthday = models.DateField(default=date(1996, 11, 28))
    website = models.CharField(max_length=40)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=10)
    age = models.IntegerField(default=calculate_age(
        date(1996, 11, 28)), editable=False)  # date is hardcoded..........
    degree = models.CharField(max_length=50)
    email = models.EmailField()
    freelance = models.BooleanField()
    interestes = models.TextField()

    def __str__(self):
        return self.name


class adminService(models.Model):
    serviceNameMajor = models.TextField()
    serviceNameMinor = models.TextField()
