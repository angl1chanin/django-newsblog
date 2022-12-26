from django import template

from news.models import Article

register = template.Library()


@register.inclusion_tag('news/tags/main-news.html')
def main_grid_articles():
    articles = Article.objects.all()[:9]
    card_types = ['solid', 'split', 'solid', 'split', 'split', 'split', 'solid', 'split', 'split']

    return {
        'articles': zip(card_types, articles),
    }
