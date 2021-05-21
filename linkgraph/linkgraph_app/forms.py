from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import Writer


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Writer
        fields = ('username', 'email', 'is_editor')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Writer
        fields = ('username', 'email')
