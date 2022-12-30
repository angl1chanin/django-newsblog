from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# App imports
from news.models import Category, Article
from news.forms import ArticleForm

# External apps imports
from accounts.models import User


class HomeView(ListView):
    model = Article
    template_name = 'news/home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.all()[9:]


def create(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('news:home')

    context = {
        'form': form,
    }

    return render(request, 'news/create.html', context=context)


def authors(request):
    return render(request, 'news/authors.html')


class ArticleView(DetailView):
    model = Article
    template_name = 'news/article.html'
    slug_field = 'slug'
    slug_url_kwarg = 'article_title'


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


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'


class CategoryView(ListView):
    model = Article
    template_name = 'news/category-detail.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.filter(category__slug=self.kwargs.get('category'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryView, self).get_context_data()
        context.update({
            'current_category': Category.objects.get(slug=self.kwargs.get('category'))
        })
        return context
