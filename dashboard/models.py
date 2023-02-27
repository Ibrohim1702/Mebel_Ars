from django.db import models
from django.utils.text import slugify

from account.models import User
# Create your models here.



def price_choice():
    return [
        ("$", "$"),
        ("Sum", "Sum"),
        ("Rub", "Rub"),
    ]


class Category(models.Model):
    img = models.ImageField(upload_to="sayt")
    content = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)
            return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.content


class Product(models.Model):
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    price_type = models.CharField(max_length=10, choices=price_choice())
    len = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    is_bed = models.BooleanField(default=False)
    bed_len = models.IntegerField(null=True, blank=True)
    bed_width = models.IntegerField(null=True, blank=True)
    bed_height = models.IntegerField(null=True, blank=True)




