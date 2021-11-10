from django.db import models
from datetime import datetime
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.FileField(blank=True)
    date = models.DateTimeField(blank=True, null=True)
    # author = models.ForeignKey('User', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

    def published(self):
        self.date = timezone.now()
        self.save()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.author_name
