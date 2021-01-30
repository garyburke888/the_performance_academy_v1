from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Article

from .forms import ArticleForm

# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/blog.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/blog_detail.html'


@login_required
def add_article(request):
    """ Add an article to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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
