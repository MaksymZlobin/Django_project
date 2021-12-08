from rest_framework import serializers

from news.models import Article, User, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'picture', 'date', 'author']


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    class Meta:
        model = Comment
        fields = ['id', 'article', 'author', 'comment_text', 'date']


class ArticleDetailSerializer(ArticleSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ArticleSerializer.Meta.fields + ['comments']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
