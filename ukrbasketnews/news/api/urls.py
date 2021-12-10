from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from news.api.api_views import ArticlesListCreateAPIView, ArticleDetailAPIView, RegisterView, CheckView


urlpatterns = [
    path('articles/', ArticlesListCreateAPIView.as_view(), name='articles'),
    path('articles/<int:article_id>/', ArticleDetailAPIView.as_view(), name='article'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('check/', CheckView.as_view()),
]
