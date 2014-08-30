from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404 

from cat_nav.models import product_categories, page_container

class CategoryList(ListView):
    model = product_categories

def details(request, page_categories_id, page_container_id): 
    page = get_object_or_404(page_container, pk=page_container_id)
    return render(request, 'cat_nav/content.html', {'page': page})

