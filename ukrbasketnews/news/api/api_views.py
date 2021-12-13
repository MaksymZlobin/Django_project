from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, get_object_or_404, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


from news.models import Article, Comment, User
from news.api.serializers import ArticleSerializer, ArticleDetailSerializer, RegisterSerializer
from news.api.permissions import IsAuthor, IsAnonymousUser
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_payload_handler


class ArticlesListCreateAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

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
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        user = request.user
        logout(request)
        OutstandingToken.objects.filter(user=user).update(expired_date=now)
        return Response(status=status.HTTP_200_OK)


