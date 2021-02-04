from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Article

from .forms import ArticleForm


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/blog.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/blog_detail.html'


@login_required
def add_article(request):
    """ Add an article to the blog, only available to superuser """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            messages.success(request, 'Successfully added article!')
            return redirect(reverse('blog_detail', args=[article.id]))
        else:
            messages.error(request, 'Failed to add article. Please ensure the form is valid.')
    else:
        form = ArticleForm()

    template = 'articles/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_article(request, article_id):
    """ Edit an article in the blog, only available to superuser """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated article!')
            return redirect(reverse('blog_detail', args=[article.id]))
        else:
            messages.error(request, 'Failed to update article. Please ensure the form is valid.')
    else:
        form = ArticleForm(instance=article)
        messages.info(request, f'You are editing {article.title}')

    template = 'articles/edit_article.html'
    context = {
        'form': form,
        'article': article,
    }

    return render(request, template, context)


@login_required
def delete_article(request, article_id):
    """ Delete an article from the blog, only available to superuser """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    messages.success(request, 'Article deleted!')
    return redirect(reverse('blog'))
