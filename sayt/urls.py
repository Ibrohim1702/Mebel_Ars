from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("cart", cart, name="cart"),
    path("ctg/", catalog, name="catalog"),
    path("cmp/", compare, name="cmp"),
    path("cntc/", contacts, name="cntc"),
    path("product/", product, name="product"),

]
