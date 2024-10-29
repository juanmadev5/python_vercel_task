from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    params = {
        'articles': articles,
    }
    return render(request, 'blog/index.html', params)


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid(): 
            article_form.save()
            return redirect('index')
    else:
        article_form = ArticleForm()

    params = {
        'form': article_form,
    }
    return render(request, 'blog/create.html', params)


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    params = {
        'article': article,
    }
    return render(request, 'blog/detail.html', params)


def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('detail', article_id)
    else:
        article_form = ArticleForm(instance=article)

    params = {
        'article': article,
        'form': article_form,
    }
    return render(request, 'blog/edit.html', params)


def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if (request.method == 'POST'):
        article.delete()
        return redirect('index')
    else:
        params = {
            'article': article,
        }
        return render(request, 'blog/delete.html', params)

from django.shortcuts import redirect

def home(request):
    return redirect('index')
