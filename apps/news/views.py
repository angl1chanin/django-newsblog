from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# App imports
from news.models import Category, Article

# External apps imports
from accounts.models import User


class HomeView(ListView):
    model = Article
    template_name = 'news/home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.all()[9:]


class ProfileView(DetailView, LoginRequiredMixin):
    model = User
    template_name = 'news/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        context.update({
            'user_articles': Article.objects.filter(author__username=self.request.user.username)
        })
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, username=self.request.user.username)


class ProfileDetailView(DetailView):
    model = User
    template_name = 'news/profile.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.username == self.kwargs.get('username'):
            return redirect('news:profile')
        return super(ProfileDetailView, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data()
        context.update({
            'user_articles': Article.objects.filter(author__username=self.kwargs.get('username'))
        })
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, username=self.kwargs.get('username'))


def category_detail_list(request, category):
    articles = Article.objects.filter(category__slug=category)
    current_category = Category.objects.get(slug=category)

    context = {
        'articles': articles,
        'current_category': current_category
    }

    return render(request, 'news/category-detail.html', context=context)


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'


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
