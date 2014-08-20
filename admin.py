from django.contrib import admin
from cat_nav.models import page_container, product_categories

class PageAdmin(admin.ModelAdmin):
    fields = [('page_title', 'page_categories'), 'page_content']
    list_display = ('page_title', 'page_categories')

admin.site.register(page_container, PageAdmin)

admin.site.register(product_categories) 
