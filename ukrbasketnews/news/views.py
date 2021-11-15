from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

from news.models import Article, Comment


def articles_list(request):
    articles_list = Article.objects.order_by('-date')[:5]
    template = loader.get_template('news/list.html')
    context = {
        'articles_list': articles_list,
    }
    return HttpResponse(template.render(context, request))


def article_detail(request, article_id):
    article = Article.objects.filter(id=article_id).first()
    if article:
        latest_comments = article.comment_set.order_by('-id')[:10]
        return render(request, 'news/detail.html', {'article': article, 'latest_comments': latest_comments})
    return render(request, '404.html')


def leave_comment(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return Http404('Article not found!')

    article.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:article', args=(article.id,)))

