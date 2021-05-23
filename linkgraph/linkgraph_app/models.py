from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import ArticleStatusTypes


class Writer(AbstractUser):
    is_editor = models.BooleanField(default=False)

    def __str__(self):
        return self.username + " editor:" + str(self.is_editor)


class Article(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    status = models.IntegerField(choices=ArticleStatusTypes.choices(), default=1)
    written_by = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='written_by_writer', unique=False)
    edited_by = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='edited_by_writer', blank=True, null=True)

    def __str__(self):
        return self.title + " " + str(self.created_at) + " " + ArticleStatusTypes(self.status).name
