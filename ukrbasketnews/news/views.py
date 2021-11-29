from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, FormView

from news.forms import ArticleForm, CommentForm
from news.models import Article, Comment


class ArticlesListView(ListView):
    template_name = 'news/list.html'
    model = Article
    queryset = Article.objects.order_by('-date')


class ArticleDetailView(DetailView):
    template_name = 'news/detail.html'
    queryset = Article.objects.all()

    def get_context_data(self, **kwargs):
        """Insert comment form and comment queryset into the context dict."""
        context = super().get_context_data(**kwargs)
        article = self.get_object(self.queryset)
        comments = article.comments.order_by('-id')
        comment_form = CommentForm()
        context.update({'comments': comments, 'comment_form': comment_form})
        return context

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect('news:page_not_found')

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class CreateCommentView(CreateView):
    model = Comment

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        article_id = self.kwargs.get('pk')
        data['article'] = article_id
        form = CommentForm(data)
        if form.is_valid():
            form.save()
            return redirect('news:article', pk=article_id)
        return redirect('news:bad_request')


class CreateArticleView(FormView):
    template_name = 'news/article_edit.html'
    form_class = ArticleForm
    success_url = '/articles/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            new_article = form.save()
            return redirect('news:article', pk=new_article.id)


class MainView(TemplateView):
    template_name = 'news/main_page.html'


class AboutView(TemplateView):
    template_name = 'news/about.html'


class NotFoundView(TemplateView):
    template_name = '404.html'


class BadRequestView(TemplateView):
    template_name = 'bad_request.html'
