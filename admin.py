from django.contrib import admin
from cat_nav.models import page_container, product_categories

class PageAdmin(admin.ModelAdmin):
    # page container overview, show categories next to titles
    list_display = ('page_title', 'page_categories')
    # page container edit page: show title and category in same field, then the content.
    fields = [('page_title', 'page_categories'), 'page_content']

admin.site.register(page_container, PageAdmin)

admin.site.register(product_categories) 
