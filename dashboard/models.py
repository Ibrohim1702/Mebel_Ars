from django.db import models
from django.utils.text import slugify

from account.models import User

class Category(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.key = slugify(self.name_uz)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_uz


def price_choice():
    return [
        ("$", "$"),
        ("Sum", "Sum"),
        ("Rub", "Rub"),
    ]

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.CharField(max_length=256)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    height = models.CharField(max_length=128)
    width = models.CharField(max_length=128)
    length = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    material = models.CharField(max_length=128, default="MDF")
    price_type = models.CharField(max_length=10, choices=price_choice())
    img = models.ImageField()
    img1 = models.ImageField()
    def __str__(self):
        return self.name


class Likes(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)



