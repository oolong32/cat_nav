from django.http import Http404
from django.shortcuts import render

from cat_nav.models import product_categories, page_container

"""
Die Views sollten vielleicht anders heissen, bzw. ist "cat-nav" in der URL unbefriedigend.
Ebenfalls unbefriedigend ist die anzeige von numerischen id's in der URL statt Namen von Kategorien und Produkten.
"""

def index(request):
    category_list = product_categories.objects.order_by('category_order')
    context = {'category_list': category_list}
    return render(request, 'cat_nav/index.html', context)

def products(request, page_categories_id)
    try:
        product = page_container.objects.get(pk=page_categories_id)
    except page_container.objects.DoesNotExist:
        raise Http404
    return render(request, 'cat_nav/products.html', {'product': product})
    
#     return HttpResponse("You're looking at the List of Pages in Category %s." % page_categories_id)

def details(request, page_categories_id): 
    pass
    # return HttpResponse("You're looking at page %s." % page_categories_id)


