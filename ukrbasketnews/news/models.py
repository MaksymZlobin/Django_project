from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.email


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.FileField(blank=True)
    date = models.DateTimeField(blank=True, null=True, auto_now=True)
    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        author = 'deleted user'
        if self.author:
            author = self.author
        return f'Article "{self.title}" - by {author}'

    def published(self):
        self.date = timezone.now()
        self.save()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    comment_text = models.CharField(max_length=200)
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        author = 'Guest'
        if self.author:
            author = self.author
        return f'Comment ID {self.pk} - article {self.article} (ID {self.article.id}) - by {author}'
