from django.contrib.auth.views import LogoutView
from django.urls import path

from news.api.api_views import ArticlesListAPIView, ArticleDetailAPIView


urlpatterns = [
    # path('', views.MainView.as_view(), name='main'),
    # path('about/', views.AboutView.as_view(), name='about'),
    path('articles/', ArticlesListAPIView.as_view(), name='articles'),
    path('articles/<int:article_id>/', ArticleDetailAPIView.as_view(), name='article'),
    # path('articles/<int:pk>/new-comment/', views.CreateCommentView.as_view(), name='create_comment'),
    # path('articles/create-article/', views.CreateArticleView.as_view(), name='create_article'),
    # path('page-not-found/', views.NotFoundView.as_view(), name='page_not_found'),
    # path('bad-request/', views.BadRequestView.as_view(), name='bad_request'),
    # path('login/', views.UserLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', views.RegisterView.as_view(), name='register'),
    # path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    # path('password/', views.PasswordView.as_view(), name='password_change'),
    # path('forbidden/', views.ForbiddenView.as_view(), name='forbidden'),
]
