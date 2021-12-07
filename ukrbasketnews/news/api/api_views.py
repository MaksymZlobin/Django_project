from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, get_object_or_404, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from news.models import Article, Comment, User
from news.api.serializers import ArticleSerializer, ArticleDetailSerializer
from news.api.permissions import IsAuthor
from rest_framework.views import APIView


class ArticlesListAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny(), ]
        elif self.request.method == 'POST':
            return [IsAuthor(), ]


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_url_kwarg = 'article_id'


# class LoginView(APIView):
#     queryset = User.objects.all()
#     permission_classes = [AllowAny, ]
#
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user:
#             login(request, user)
#             return Response(status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
