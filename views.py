from django.views.generic import ListView, DetailView

from cat_nav.models import product_categories, page_container

class SimpleCategoryList(ListView):
    model = product_categories
    context_object_name = 'all_categories'
    template_name = 'cat_nav/simple_categories.html'

class CategoryListDeluxe(ListView):
    model = product_categories
    context_object_name = 'all_categories_and_some'
    def get_context_data(self, **kwargs):
        context = super(CategoryListDeluxe, self).get_context_data(**kwargs)
        urlKey = self.kwargs['pk']
        context['my_category'] = product_categories.objects.get(pk=urlKey)
        return context

class PageDetails(DetailView):
    model = page_container
    context_object_name = 'product' 
