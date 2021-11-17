from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.utils import timezone


from news.models import Article, Comment
from news.forms import ArticleForm, CommentForm


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


def create_comment(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.author_name = request.POST['name']
            form.comment_text = request.POST['text']
            form.save()
            article = Article.objects.get(id=article_id)
            return redirect('news:article', id=article.id)
    else:
        form = CommentForm()
    return render(request, 'news/comment.html', {'form': form})


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return redirect('news:article', article_id=new_article.id)
    else:
        form = ArticleForm()
    return render(request, 'news/article_edit.html', {'form': form})
