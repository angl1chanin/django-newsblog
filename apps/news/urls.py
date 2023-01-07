from django.urls import path

from news.views import (
    HomeView, ProfileView, ProfileDetailView, CategoryListView,
    CategoryView, ArticleView, ArticleCreateView, AuthorsListView,
    TagsView, fav_add, fav_list, fav_clear
)

app_name = 'news'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('create/', ArticleCreateView.as_view(), name='create-article'),
    path('authors/', AuthorsListView.as_view(), name='authors-list'),
    path('tags/', TagsView.as_view(), name='tags-list'),

    path('favourites/', fav_list, name='favourites-list'),
    path('favourites-clear/', fav_clear, name='favourites-clear'),
    path('favourites/<int:pk>', fav_add, name='favourites'),

    path('news/<slug:category>/<slug:article_title>', ArticleView.as_view(), name='article-detail'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>', ProfileDetailView.as_view(), name='profile-detail'),

    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('news/<slug:category>', CategoryView.as_view(), name='category'),
]
