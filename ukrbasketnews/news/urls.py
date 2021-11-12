from django.urls import path

from news.views import articles_list, article_detail

app_name = 'articles'
urlpatterns = [
    path('', articles_list, name='articles'),
    path('<int:article_id>/', article_detail, name='article'),
]
