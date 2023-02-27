from django.db import models


# Create your models here.


class Employees(models.Model):
    ism_familya = models.CharField(max_length=256)
    yoshi = models.IntegerField(null=True)
    lavozimi = models.CharField(max_length=256)
    salary = models.IntegerField()
    city = models.CharField(choices=[
        ("Toshkent", "Toshkent"),
        ("Andijon", "Andijon"),
        ("Farg`ona", "Farg`ona"),
        ("Namangan", "Namangan"),
        ("Qashqadaryo", "Qashqadaryo"),
        ("Surxandaryo", "Surxandaryo"),
        ("Buxoro", "Buxoro"),
        ("Samarqand", "Samarqand"),
        ("Jizzax", "Jizzax"),
        ("Navoiy", "Navoiy"),
        ("Sirdaryo", "Sirdaryo"),
        ("Xorazm", "Xorazm"),

    ], max_length=125, null=True)

    def __str__(self):
        return self.ism_familya


class Contact(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.phone}"


class Bascade(models.Model):
    pass