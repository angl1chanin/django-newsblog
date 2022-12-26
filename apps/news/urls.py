from django.urls import path
from news.views import home, profile, profile_detail, categories, authors, article, create, category_detail_list

app_name = 'news'

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create-article'),
    path('authors/', authors, name='authors-list'),

    path('news/<slug:category>/<slug:article_title>', article, name='article-detail'),

    path('profile/', profile, name='profile'),
    path('profile/<str:username>', profile_detail, name='profile-detail'),

    path('categories/', categories, name='categories-list'),
    path('news/<slug:category>', category_detail_list, name='category'),
]
