from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from .models import User


# Create your views here.

def sign_up(requests):
    if requests.POST:
        username = requests.POST.get('username')
        password = requests.POST.get('pass')
        re_pass = requests.POST.get('re_pass')
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        if password != re_pass:
            ctx = {
                "error": True
            }
            return render(requests, 'registration/register.html', ctx)

        user = User.objects.filter(username=username).first()

        if user:
            ctx = {
                "error": True
            }
            return render(requests, 'registration/register.html', ctx)

        root = User()
        root.name = name
        root.phone = phone
        root.username = username
        root.password = password
        root.save()

        authenticate(requests)
        login(requests, root)

        return redirect('home')

    ctx = {

    }
    return render(requests, 'registration/register.html', ctx)


def sign_in(requests):
    if requests.POST:
        username = requests.POST.get('username')
        password = requests.POST.get('pass')

        user = User.objects.filter(username=username).first()
        if not user:
            print("a")
            ctx = {
                "error": True
            }
            return render(requests, 'registration/login.html', ctx)

        if not user.check_password(password):
            print("b")
            ctx = {
                "error": True
            }
            return render(requests, 'registration/login.html', ctx)
        print("c")
        login(requests, user)

        return redirect('home')

    ctx = {

    }
    return render(requests, "registration/login.html")


def sign_out(requests, conf=False):
    if not conf:
        return render(requests, "registration/conf_out.html")
    logout(requests)

    return redirect("sign_in")
