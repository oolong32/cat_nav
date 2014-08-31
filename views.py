from django.views.generic import ListView, DetailView
# from django.shortcuts import render, get_object_or_404 

from cat_nav.models import product_categories, page_container

class CategoryList(ListView):
    model = product_categories

class PageDetails(DetailView):
    model = page_container
    context_object_name = 'product'
    # queryset should be filtered for the respective category
    # that is: '1' must be replaced by 'page_categories_id' but how to access?
    # or it shouldn't: the category is mainly needed to add a class name to the html in order to highlight the "active" category in the menu.
    pk_url_kwarg = 'product_id'

# def details(request, page_categories_id, page_container_id): 
#     page = get_object_or_404(page_container, pk=page_container_id)
#     return render(request, 'cat_nav/content.html', {'page': page})

