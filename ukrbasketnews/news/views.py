from django.shortcuts import render
from django.http import HttpResponse
from news.models import Article



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def articles_list(request):
    return HttpResponse('You are looking for articles.')


def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return HttpResponse('Such article does not exist')
    return HttpResponse(f'You are looking at the #{article} article')


