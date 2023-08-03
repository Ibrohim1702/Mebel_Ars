from django.contrib import admin
from .models import User, Product, Category
from sayt.models import Contact
# Register your models here.

admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Category)