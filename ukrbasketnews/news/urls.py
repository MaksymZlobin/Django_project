from django.urls import path

from news import views

app_name = 'news'
urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('articles/', views.ArticlesListView.as_view(), name='articles'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article'),
    path('articles/<int:pk>/new-comment/', views.CreateCommentView.as_view(), name='create_comment'),
    path('articles/new-article/', views.CreateArticleView.as_view(), name='create_article'),
    path('page-not-found/', views.NotFoundView.as_view(), name='page_not_found'),
    path('bad-request/', views.BadRequestView.as_view(), name='bad_request'),
]
