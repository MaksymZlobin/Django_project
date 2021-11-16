from django.urls import path

from news.views import articles_list, article_detail, leave_comment, create_article

app_name = 'news'
urlpatterns = [
    path('', articles_list, name='articles'),
    path('<int:article_id>/', article_detail, name='article'),
    path('<int:article_id>/leave_comment', leave_comment, name='leave_comment'),
    path('create_article/', create_article, name='create_article'),
]
