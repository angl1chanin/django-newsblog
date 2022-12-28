from django.urls import path

from news.views import authors, article, create, category_detail_list
from news.views import HomeView, ProfileView, ProfileDetailView, CategoryListView

app_name = 'news'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', create, name='create-article'),
    path('authors/', authors, name='authors-list'),

    path('news/<slug:category>/<slug:article_title>', article, name='article-detail'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>', ProfileDetailView.as_view(), name='profile-detail'),

    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('news/<slug:category>', category_detail_list, name='category'),
]
