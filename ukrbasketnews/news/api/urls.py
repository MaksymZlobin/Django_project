from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from news.api.api_views import ArticlesListAPIView, ArticleDetailAPIView, LoginView, RegisterView


urlpatterns = [
    path('articles/', ArticlesListAPIView.as_view(), name='articles'),
    path('articles/<int:article_id>/', ArticleDetailAPIView.as_view(), name='article'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
