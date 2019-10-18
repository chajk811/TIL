from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})
    
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()
    return render(request, 'articles/create.html', {'article_form': article_form})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comment_form = CommentForm()
    return render(request, 'articles/detail.html', {'article': article, 'comment_form': comment_form})

def update(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    return render(request, 'articles/update.html', {'article_form': article_form})

def delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return redirect('articles:index')
    
@require_POST
def comments_create(request, article_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save()
    return redirect('articles:detail', article_id)

@require_POST
def comments_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('articles:detail', article_id)
