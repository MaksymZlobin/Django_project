from django.urls import path

from news.views import articles_list, article_detail

urlpatterns = [
    path('', articles_list, name='articles'),
    path('<int:id>/', article_detail, name='article'),
]
