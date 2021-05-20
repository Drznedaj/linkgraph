from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm

# Create your views here.


def dashboard(request):
    return render(
        request,
        "app/dashboard.html",
    )


def register(request):
    form = CustomUserCreationForm(request.POST or None)

    if form.is_valid():

        user = form.save()

        login(request, user)

        return redirect(reverse("dashboard"))

    return render(request, "app/register.html", {"form": form})
