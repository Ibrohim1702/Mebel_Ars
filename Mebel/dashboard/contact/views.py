from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from sayt.models import Contact


def list(requests, pk=None):
    cntc = Contact.objects.all()
    ctx = {
        "cntc": cntc,
        "all": Contact.objects.all(),
        "cnt_html": True
    }
    if pk:
        root = Contact.objects.get(pk=pk)
        root.read = False
        ctx = {
            "root": root,
            "cnt_html": True
        }
        return render(requests, "dashboard/contact/detail.html", ctx)
    else:

        return render(requests, "dashboard/contact/list.html", ctx)


def detail(requests, pk):
    cntc = Contact.objects.get(pk=pk)
    ctx = {
        "cntc": cntc

    }
    return render(requests, "dashboard/contact/detail.html", ctx)


@staff_member_required(login_url="dash_login")
def delete(requests, pk):
    Contact.objects.get(pk=pk).delete()
    return redirect("ctg_list")
