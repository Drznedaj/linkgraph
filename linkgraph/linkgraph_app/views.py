from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm

from .models import Writer, Article
from .forms import ArticleForm
import datetime


def dashboard(request):
    table_data = []
    writers = Writer.objects.all()
    last_thirty_days = datetime.datetime.now() - datetime.timedelta(30)

    for w in writers:
        written_count = Article.objects.filter(written_by=w).count()
        written_last_count = Article.objects.filter(written_by=w, created_at__gt=last_thirty_days).count()
        table_data.append((w.username, written_count, written_last_count))

    print(table_data)
    return render(
        request,
        "app/dashboard.html",
        {"table_data": table_data},
    )


def register(request):
    form = CustomUserCreationForm(request.POST or None)

    if form.is_valid():

        user = form.save()

        login(request, user)

        return redirect(reverse("dashboard"))

    return render(request, "app/register.html", {"form": form})


def create(request):

    form = ArticleForm(request.POST or None)

    if form.is_valid():
        candidate = form.save(commit=False)
        before = datetime.datetime.now() - datetime.timedelta(60)
        candidate.created_at = before
        candidate.written_by = request.user
        candidate.save()
        return redirect(reverse("dashboard"))

    return render(request, "app/create.html", {"form": form})
