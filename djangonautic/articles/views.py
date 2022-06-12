from django.shortcuts import render
from .models import Article

# Create your views here.
def home_page(request):
    """"Function return to client the home page """
    return render(request, 'layout_area/layout/base_layout.html')

def article_lists(request):
    """"Function return all articles objects from DB  to client"""
    articles = Article.objects.all().order_by('date')
    print(articles)
    return render(request, 'home_page/articles/article_lists.html', {'articles': articles})

def article_detail(request,slug):
    """"Function return  article objects according to  client slug"""
    # ???? How To pass slug directly to render(...,...,slug or {slug:slug})
    article = Article.objects.get(slug=slug)

    return render(request, 'home_page/articles/article_detail.html', {'article': article})
