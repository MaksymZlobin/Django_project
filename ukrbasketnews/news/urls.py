from django.urls import path

from news.views import articles_list, article_detail, create_comment, create_article

app_name = 'news'
urlpatterns = [
    path('', articles_list, name='articles'),
    path('<int:article_id>/', article_detail, name='article'),
    path('<int:article_id>/create_comment', create_comment, name='create_comment'),
    path('create_article/', create_article, name='create_article'),
]
