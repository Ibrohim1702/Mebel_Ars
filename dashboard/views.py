from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.shortcuts import render, redirect

from account.models import User
from dashboard.forms import UserForm
from sayt.models import Contact


# Create your views here.
@staff_member_required(login_url="dash_login")
def index(requests):
    contacts = Contact.objects.filter(read=False)

    ctx = {
        "contacts": contacts,
        "cnt_c": contacts.count


    }
    return render(requests, "dashboard/base.html", ctx)


def dashboard_login(requests):
    if requests.POST:
        username = requests.POST.get("username")
        pas = requests.POST.get("pass")
        user = User.objects.filter(username=username).first()

        if not user:
            ctx = {
                "error": True
            }

            return render(requests, "dashboard/login.html", ctx)

        if not user.check_password(pas):
            ctx = {
                "error": True
            }

            return render(requests, "dashboard/login.html", ctx)
        login(requests, user)
        return redirect("dashboard")
    return render(requests, "dashboard/login.html")


@staff_member_required(login_url="dash_login")
def edit_user(requests):
    if requests.POST:

        requests.user.username = requests.POST.get("username")
        requests.user.phone = requests.POST.get("phone")
        requests.user.first_name = requests.POST.get("first_name")
        requests.user.last_name = requests.POST.get("last_name")
        requests.user.location = requests.POST.get("location")
        requests.user.bio = requests.POST.get("bio")
        requests.user.save()

    ctx = {

    }
    return render(requests, 'dashboard/user.html', ctx)


