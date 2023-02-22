from django.contrib import admin
from .models import Employees
from sayt.models import Contact
# Register your models here.

admin.site.register(Employees)
admin.site.register(Contact)