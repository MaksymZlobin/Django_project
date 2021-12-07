from django.contrib.auth.views import LogoutView
from django.urls import path

from news.api.api_views import ArticlesListAPIView, ArticleDetailAPIView


urlpatterns = [
    path('articles/', ArticlesListAPIView.as_view(), name='articles'),
    path('articles/<int:article_id>/', ArticleDetailAPIView.as_view(), name='article'),
    # path('login/', LoginView.as_view(), name='login'),
]
