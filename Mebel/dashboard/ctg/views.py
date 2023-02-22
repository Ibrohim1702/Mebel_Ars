from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

from dashboard.ctg.forms import CtgForm
from dashboard.models import Category
from sayt.models import Employees


def list(requests):
    ctgs = Employees.objects.all()
    ctx = {
        "ctgs": ctgs
    }
    return render(requests, "dashboard/ctg/list.html", ctx)


def detail(requests, pk):
    ctg = Employees.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/ctg/detail.html", ctx)


@staff_member_required(login_url="dash_login")
def add(requests):
    forms = CtgForm()
    if requests.POST:
        form = CtgForm(requests.POST, requests.FILES)
        if form.is_valid():
            form.save()
            return redirect('ctg_list')
        else:
            print(form.errors)

    ctx = {
        "forms": forms
    }
    return render(requests, "dashboard/ctg/form.html", ctx)


@staff_member_required(login_url="dash_login")
def edit(requests, pk):
    root = Employees.objects.get(pk=pk)
    forms = CtgForm(instance=root)

    if requests.POST:
        form = CtgForm(requests.POST, requests.FILES, instance=root)
        if form.is_valid():
            form.save()
            return redirect('ctg_list')
        else:
            print(form.errors)

    ctx = {
        "forms": forms,
        "root": root
    }
    return render(requests, "dashboard/ctg/form.html", ctx)


@staff_member_required(login_url="dash_login")
def delete(requests, pk):
    Employees.objects.get(pk=pk).delete()
    return redirect("ctg_list")
