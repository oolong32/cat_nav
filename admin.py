from django.contrib import admin
from cat_nav.models import page_container, product_categories

class PageAdmin(admin.ModelAdmin):
    # page container overview, show categories next to titles
    list_display = ('page_title', 'page_categories')
    # page container edit page: show title and category in same field, then the content.
    fields = [('page_title', 'page_categories'), 'page_content']
    # filter pages by categories
    list_filter = ['page_categories']

admin.site.register(page_container, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    """
    It's not really neccessary to have an extra model for the categories,
    but you never know.
    """
    fields = ['category_name', 'category_order']
    
admin.site.register(product_categories, CategoryAdmin) 
