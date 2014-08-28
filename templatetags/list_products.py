from django import template
from cat_nav.models import page_container
register = template.Library()

def list_products(product):
    # now how do I filter this?
    # here or in the template?
    product_list = page_container.objects.all
    return {'product_list': product_list}

register.inclusion_tag('cat_nav/list_products.html')(list_products)
