from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import ModelForm, CharField, Textarea
from news.models import Article, Comment, User


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'picture', 'author']


class CommentForm(ModelForm):
    comment_text = CharField(widget=Textarea, label='Enter comment text', max_length=200)

    class Meta:
        model = Comment
        fields = ['article', 'author', 'comment_text']


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
