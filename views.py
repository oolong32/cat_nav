from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404 

from cat_nav.models import product_categories, page_container

class CategoryList(ListView):
    model = product_categories

class PageDetails(DetailView):
    context_object_name = 'product'
    queryset = page_container.objects.all()
    # queryset should be filtered for the respective category
    pk_url_kwarg = 'page_container_id'

# def details(request, page_categories_id, page_container_id): 
#     page = get_object_or_404(page_container, pk=page_container_id)
#     return render(request, 'cat_nav/content.html', {'page': page})

