from django.contrib.auth.views import LoginView
from django.urls import path

from API.v1.auth.views import UserActionsView
# from API.v1.auth.views import *
from API.v1.employees.views import UserView

urlpatterns = [
    path("usr/", UserView.as_view()),
    path("usr/<int:pk>/", UserView.as_view()),
    # path("auth/", AuthView.as_view()),
    path("action/", UserActionsView.as_view())
]
