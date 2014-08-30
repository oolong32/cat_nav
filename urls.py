from django.conf.urls import patterns, url

from cat_nav.views import CategoryList, PageDetails
from cat_nav import views

urlpatterns = patterns('',
    url(r'^$', CategoryList.as_view()),
    # url(r'^(?P<page_categories_id>\d+)/$', views.products, name='products'),
    url(r'^(?P<page_categories_id>\d+)/(?P<page_container_id>\d+)/$', PageDetails.as_view()),
)
"""
Der Index sollte alle Kategorien "gefaltet" zeigen.
Dazu sollte es eine url mit kategorienamen als slug geben, der die jew. kategorie "ausgefaltet" zeigt.
"""
