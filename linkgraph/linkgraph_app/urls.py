from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("article/", views.create, name="create"),
    path("article-approval/", views.article_approval, name="article_approval"),
    path("approve/<int:article_id>", views.approve, name="approve"),
    path("reject/<int:article_id>", views.reject, name="reject"),
]
