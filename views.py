from django.views.generic import ListView, DetailView

from cat_nav.models import product_categories, page_container

class CategoryList(ListView):
    model = product_categories
    context_object_name = 'all_categories'
    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        urlKey = self.kwargs['pk']
        context['my_category'] = product_categories.objects.get(pk=urlKey)
        return context

class PageDetails(DetailView):
    model = page_container
    context_object_name = 'product' 
