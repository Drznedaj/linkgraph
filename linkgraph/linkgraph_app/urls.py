from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.dashboard, name="dashboard"),
]