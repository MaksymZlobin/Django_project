from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from news.models import Article


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def articles_list(request):
    articles_list = Article.objects.order_by('date')[:5]
    template = loader.get_template('news/index.html')
    context = {
        'articles_list': articles_list,
    }
    return HttpResponse(template.render(context, request))


def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return HttpResponse('Such article does not exist')
    return HttpResponse(f'You are looking at the #{article} article')


