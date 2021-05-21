from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import Writer, Article


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Writer
        fields = ('username', 'email', 'is_editor')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Writer
        fields = ('username', 'email')


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content', 'status')

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['status'].disabled = True
