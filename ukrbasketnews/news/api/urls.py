from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from news.api.api_views import (
    ArticlesListCreateAPIView,
    ArticleDetailAPIView,
    CommentCreateAPIView,
    CheckAPIView,
    LogoutAPIView,
    RegisterAPIView,
    ProfileAPIView,
    PasswordChangeAPIView,
)


urlpatterns = [
    path('articles/', ArticlesListCreateAPIView.as_view(), name='articles'),
    path('articles/<int:article_id>/', ArticleDetailAPIView.as_view(), name='article'),
    path('articles/<int:article_id>/new-comment', CommentCreateAPIView.as_view(), name='comment'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('profile/<int:user_id>/', ProfileAPIView.as_view(), name='profile'),
    path('password-change/', PasswordChangeAPIView.as_view(), name='password_change'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('check/', CheckAPIView.as_view()),
]
