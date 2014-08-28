from djago.views.generic import ListView
from django.shortcuts import render, get_object_or_404 

from cat_nav.models import product_categories, page_container

"""
Die Views sollten vielleicht anders heissen, bzw. ist "cat-nav" in der URL unbefriedigend.
Ebenfalls unbefriedigend ist die anzeige von numerischen id's in der URL statt Namen von Kategorien und Produkten.
"""

class CategoryList
    model = product_categories

# def index(request):
#     category_list = product_categories.objects.order_by('category_order')
#     context = {'category_list': category_list}
#     return render(request, 'cat_nav/index.html', context)

def products(request, page_categories_id):
    product = get_object_or_404 (product_categories, pk=page_categories_id)
    return render(request, 'cat_nav/products.html', {'product': product})
    
def details(request, page_categories_id, page_container_id): 
    page = get_object_or_404(page_container, pk=page_container_id)
    return render(request, 'cat_nav/content.html', {'page': page})

