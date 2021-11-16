from django.forms import ModelForm
from news.models import Article, Comment, User


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'picture', 'author']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'comment_text']
