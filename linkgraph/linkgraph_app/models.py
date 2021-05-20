from django.db import models
from django.contrib.auth.models import User
from .utils import ArticleStatusTypes


class Writer(models.Model):
    is_editor = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + " editor:" + self.is_editor


class Article(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    title = models.TextField(max_length=50)
    content = models.TextField()
    status = models.IntegerField(choices=ArticleStatusTypes.choices(), default=1)
    written_by = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='written_by_writer')
    edited_by = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='edited_by_writer')

    def __str__(self):
        return self.title + " " + self.created_at + " " + self.status
