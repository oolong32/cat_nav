from django.conf.urls import patterns, url

from cat_nav import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    """
    <page_categories_id> muss durch lesbare namen ersetzt werden. durch den "category_name hinter der page_categories_id.
    """
    url(r'^(?P<page_categories_id>\d+)/$', views.products, name='products'),
    url(r'^(?P<page_categories_id>\d+)/details/$', views.details, name='details'),

