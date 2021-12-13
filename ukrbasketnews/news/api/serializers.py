from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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
    # email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    # first_name = serializers.CharField(max_length=50, required=True)
    # last_name = serializers.CharField(max_length=50, required=True)
    # password1 = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    # password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    # def validate(self, attrs):
    #     if attrs['password1'] != attrs['password2']:
    #         raise serializers.ValidationError({'password': "Password fields didn't match."})
    #     return attrs
    #
    # def create(self, validated_data):
    #     user = User.objects.create(
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name']
    #     )
    #
    #     user.set_password(validated_data['password1'])
    #     user.save()
    #
    #     return user
