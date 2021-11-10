from django.db import models
from datetime import datetime
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.FileField(blank=True)
    date = models.DateTimeField(blank=True, null=True)
    # author = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def published(self):
        self.date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('імʼя автора', max_length=50)
    comment_text = models.CharField('текст коментаря', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
