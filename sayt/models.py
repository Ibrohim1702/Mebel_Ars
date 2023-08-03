from django.db import models

from dashboard.models import Category, Product


# Create your models here.


class User(models.Model):
    Ism = models.CharField(max_length=256)
    Familiya = models.CharField(max_length=256)
    yoshi = models.IntegerField(null=True)
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
        return self.Ism


class Contact(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.phone}"


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.price = int(self.product.price) * int(self.quantity)
        return super(Basket, self).save(*args, **kwargs)

    def __str__(self):
        return self.price























