from django.shortcuts import render

from cat_nav.models import product_categories

def index(request):
    category_list = product_categories.objects.order_by('category_order')
    context = {'category_list': category_list}
    return render(request, 'cat_nav/index.html', context)

def page_content_view(request, page_categories_id):
    pass
    # return HttpResponse("You're looking at page %s." % page_categories_id)

# def category_list(request, page_categories_id):
#     return HttpResponse("You're looking at the List of Categories %s." % page_categories_id)

# def page_list(request, page_categories_id)
#     return HttpResponse("You're looking at the List of Pages in Category %s." % page_categories_id)
