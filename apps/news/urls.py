from django.urls import path

from news.views import authors, create
from news.views import HomeView, ProfileView, ProfileDetailView, CategoryListView, CategoryView, ArticleView

app_name = 'news'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', create, name='create-article'),
    path('authors/', authors, name='authors-list'),

    path('news/<slug:category>/<slug:article_title>', ArticleView.as_view(), name='article-detail'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>', ProfileDetailView.as_view(), name='profile-detail'),

    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('news/<slug:category>', CategoryView.as_view(), name='category'),
]
