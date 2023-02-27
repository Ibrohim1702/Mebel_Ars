from django.urls import path

from sayt.views import contacts
from .views import *

urlpatterns = [
    path("", list, name="contact_list"),
    path("det/<int:pk>", detail, name="contact_detail")

]
