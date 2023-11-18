from django.template import Library
from story.models import Category

register = Library()

@register.simple_tag
def get_categories(limit=10):
    print(limit)
    return Category.objects.all()[:limit]


@register.filter
def make_upper(val):
    return val.upper()