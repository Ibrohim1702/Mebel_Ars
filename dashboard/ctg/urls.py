from django.urls import path
from .views import *

urlpatterns = [
    path("", list, name="ctg_list"),
    path("detail/<int:pk>/", detail, name="ctg_detail"),
    path("add/", add, name="ctg_add"),
    path("edit/<int:pk>/", edit, name="ctg_edit"),
    path("del/<int:pk>/", delete, name="ctg_del"),

]
