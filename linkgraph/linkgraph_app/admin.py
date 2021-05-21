from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Writer, Article


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Writer
    list_display = ['email', 'username', ]


admin.site.register(Writer, CustomUserAdmin)
admin.site.register(Article)
