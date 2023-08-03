from django.shortcuts import render
from .models import *


# Create your views here.

def index(requests):
    print(requests.user)

    fresh = Product.objects.all().order_by("-pk")
    # top = ProductCtg.objects.filters("-views")

    ctx = {
        "fresh": fresh,
        # "top": top,


    }
    return render(requests, "site/index.html", ctx)


def cart(requests):
    ctx = {

    }
    return render(requests, "site/cart.html", ctx)


def catalog(requests):
    ctx = {

    }
    return render(requests, "site/catalog.html", ctx)


def compare(requests):
    ctx = {

    }
    return render(requests, "site/compare.html", ctx)


def contacts(requests):
    ctx = {

    }
    if requests.POST:
        root = Contact()
        root.name = requests.POST.get("name")
        root.phone = requests.POST.get("phone")
        root.message = requests.POST.get("message")
        root.save()
        ctx['add'] = True

    return render(requests, "site/contacts.html", ctx)


def product(requests):
    ctx = {

    }
    return render(requests, "site/product.html", ctx)
