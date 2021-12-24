from datetime import datetime
from django.contrib.auth import login, authenticate
from django.core import management
from rest_framework import status, filters
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework.views import APIView

from news.api.permissions import IsAuthor, IsAnonymousUser, IsCurrentUser
from news.api.serializers import (
    ArticleSerializer,
    ArticleDetailSerializer,
    CommentSerializer,
    RegisterSerializer,
    UserSerializer,
    PasswordChangeSerializer,
    ProfileSerializer,
    CommentCreateSerializer,
)
from news.models import Article, Comment, User


class ArticlesListCreateAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # filter_backends = [filters.OrderingFilter]
    # ordering = ['-date']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthor(), ]
        return [AllowAny(), ]

    def get_queryset(self):
        qs = self.queryset.all()
        email = self.request.query_params.get('author')
        if isinstance(email, int):
            return qs.filter(author=email)
        return qs.filter(author__email=email)


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_url_kwarg = 'article_id'


class CheckAPIView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        return Response(data={'user_is_authenticated': request.user.is_authenticated}, status=status.HTTP_200_OK)


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAnonymousUser, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
        if user:
            login(request, user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        user = request.user
        OutstandingToken.objects.filter(user=user).update(expires_at=datetime.now())
        management.call_command('flushexpiredtokens')
        return Response(data={'message': 'Success!'}, status=status.HTTP_200_OK)


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if request.user.is_authenticated:
            data['author'] = request.user.id
        data['article'] = self.kwargs.get('article_id')
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsCurrentUser, ]
    lookup_url_kwarg = 'user_id'


class PasswordChangeAPIView(UpdateAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.data.get('old_password')):
                return Response('Wrong password!', status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response('Password updated successfully!', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
