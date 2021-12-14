from datetime import datetime
from django.core import management
from rest_framework import status, filters
from rest_framework.generics import RetrieveAPIView, CreateAPIView, get_object_or_404, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework.views import APIView

from news.api.permissions import IsAuthor, IsAnonymousUser
from news.api.serializers import ArticleSerializer, ArticleDetailSerializer, RegisterSerializer
from news.models import Article, Comment, User


class ArticlesListCreateAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['-date']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthor(), ]
        return [AllowAny(), ]


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_url_kwarg = 'article_id'


class CheckView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        return Response(data={'user_is_authenticated': request.user.is_authenticated}, status=status.HTTP_200_OK)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAnonymousUser, ]


class LogOutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        user = request.user
        OutstandingToken.objects.filter(user=user).update(expires_at=datetime.now())
        management.call_command('flushexpiredtokens')
        return Response('success', status=status.HTTP_200_OK)


