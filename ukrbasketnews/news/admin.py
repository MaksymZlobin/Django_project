from django.contrib import admin
from news.models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'date')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass