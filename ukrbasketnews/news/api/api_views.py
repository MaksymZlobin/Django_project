from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from news.models import Article, Comment
from news.api.serializers import ArticleSerializer, CommentSerializer, ArticleDetailSerializer


class ArticlesListAPIView(APIView):

    def get_queryset(self):
        return Article.objects.all()

    def get(self, request):
        serializer = ArticleSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class ArticleDetailAPIView(APIView):

    def get_queryset(self):
        return Article.objects.all()

    def get_object(self, article_id):
        article = get_object_or_404(self.get_queryset(), id=article_id)
        return article

    def get(self, request, article_id):
        serializer = ArticleDetailSerializer(self.get_object(article_id))
        return Response(serializer.data)


class CommentsListAPIView(APIView):

    def get_queryset(self):
        return Comment.objects.filter(article_id=self.kwargs.get('article_id'))

    def get(self, request):
        serializer = CommentSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

