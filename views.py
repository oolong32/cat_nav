from django.views.generic import ListView, DetailView

from cat_nav.models import product_categories, page_container

class CategoryList(ListView):
    model = product_categories

class PageDetails(DetailView):
    model = page_container
    context_object_name = 'product'
    pk_url_kwarg = 'product_id' 
