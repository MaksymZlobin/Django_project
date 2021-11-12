from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from news.models import Article


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def articles_list(request):
    articles_list = Article.objects.order_by('-date')[:5]
    template = loader.get_template('news/list.html')
    context = {
        'articles_list': articles_list,
    }
    return HttpResponse(template.render(context, request))


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'news/detail.html', {'article': article})


