from django.contrib.auth.views import LoginView
from django.urls import path

from API.v1.auth.views import *
from API.v1.employees.views import EmployeesView

urlpatterns = [
    path("emp/", EmployeesView.as_view()),
    path("emp/<int:pk>/", EmployeesView.as_view()),
    path("auth/", AuthView.as_view()),
    path("action/", UserActionsView.as_view())
]