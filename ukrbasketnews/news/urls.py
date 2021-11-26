from django.urls import path

from news import views

app_name = 'news'
urlpatterns = [
    path('', views.main_page, name='main'),
    path('about/', views.about, name='about'),
    path('articles_list/', views.articles_list, name='articles'),
    path('<int:article_id>/', views.article_detail, name='article'),
    path('<int:article_id>/create_comment', views.create_comment, name='create_comment'),
    path('create_article/', views.create_article, name='create_article'),
]
