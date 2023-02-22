from django.urls import path, include

from .views import *

urlpatterns = [
    path("", index, name="dashboard"),
    path("login/", dashboard_login, name= "dash_login"),
    path("edit_profile/", edit_user, name= "edit_profile"),
    path('ctg/', include('dashboard.ctg.urls')),
    path('cntc/',  include('dashboard.contact.urls')),

]