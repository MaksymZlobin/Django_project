from django.urls import path
from main import views
from news.views import articles_list

urlpatterns = [
    path('', views.main_page, name='main'),
    path('about/', views.about, name='about'),
    path('articles_list/', articles_list, name='articles'),
]
