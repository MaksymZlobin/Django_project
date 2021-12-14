from django.contrib.auth.password_validation import validate_password
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
    password1 = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields don't match."})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
