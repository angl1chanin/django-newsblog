from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required

# App imports
from news.models import Category, Article

# External apps imports
from accounts.models import User


def home(request):
    articles = Article.objects.all()[9:]

    context = {
        'articles': articles
    }

    return render(request, 'news/home.html', context=context)


@login_required()
def profile(request):
    user = User.objects.get(username=request.user.username)
    user_articles = Article.objects.filter(author__username=request.user.username)

    context = {
        'user': user,
        'user_articles': user_articles,
    }

    return render(request, 'news/profile.html', context=context)


def profile_detail(request, username):
    user = User.objects.get(username=username)
    user_articles = Article.objects.filter(author__username=username)

    context = {
        'user': user,
        'user_articles': user_articles,
    }

    return render(request, 'news/profile.html', context=context)


def category_detail_list(request, category):
    articles = Article.objects.filter(category__slug=category)
    current_category = Category.objects.get(slug=category)

    context = {
        'articles': articles,
        'current_category': current_category
    }

    return render(request, 'news/category-detail.html', context=context)


def categories(request):
    categories_list = Category.objects.all()

    context = {
        'categories': categories_list
    }

    return render(request, 'news/categories.html', context=context)


def authors(request):
    return render(request, 'news/authors.html')


def article(request, category, article_title):
    article_detail = Article.objects.get(category__slug=category, slug=article_title)

    context = {
        'article': article_detail,
    }

    return render(request, 'news/article.html', context=context)


def create(request):
    return render(request, 'news/create.html')
