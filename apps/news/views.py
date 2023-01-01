from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# App imports
from news.models import Category, Article, Tag
from news.forms import ArticleForm
from news.utils import rename_photo_to_slug

# External apps imports
from accounts.models import User


class HomeView(ListView):
    model = Article
    template_name = 'news/home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.all()[9:]


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'news/create.html'

    # TODO: Create function for rename of an uploaded file to slug.extension format
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return HttpResponseRedirect(
                reverse_lazy(
                    'news:article-detail',
                    kwargs={
                        'category': article.category.slug,
                        'article_title': article.slug
                    }
                )
            )
        return HttpResponse("Invalid form")


class AuthorsListView(ListView):
    model = User
    template_name = 'news/authors.html'


class TagsView(ListView):
    model = Tag
    template_name = 'news/tags.html'


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
        if self.request.GET:
            if (display_type := self.request.GET.get('display')) in ['solid', 'split']:
                context.update({
                    'display_type': display_type
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
        if self.request.GET:
            if (display_type := self.request.GET.get('display')) in ['solid', 'split']:
                context.update({
                    'display_type': display_type
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
