from django.forms import ModelForm, CharField, Textarea
from news.models import Article, Comment, User


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'picture', 'author']


class CommentForm(ModelForm):
    comment_text = CharField(widget=Textarea, label='Enter comment text', max_length=200)
    default_name = 'Guest'

    class Meta:
        model = Comment
        fields = ['article', 'author', 'comment_text']


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
