from django import template
from cat_nav.models import product_categories, page_container
# page_container import not needed, is it?
register = template.Library()

def list_categories(category):
    category_list = product_categories.objects.order_by('category_order')
    return {'category_list': category_list}

register.inclusion_tag('cat_nav/list_categories.html')(list_categories)
