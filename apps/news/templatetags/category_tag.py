from django import template

from news.models import Category


register = template.Library()


@register.inclusion_tag('news/tags/categories.html')
def get_categories():
    categories = Category.objects.all()

    return {
        'categories': categories,
    }
