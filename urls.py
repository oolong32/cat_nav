from django.conf.urls import patterns, url

from cat_nav.views import SimpleCategoryList, CategoryListDeluxe, PageDetails
from cat_nav import views

urlpatterns = patterns('',
    url(r'^$', SimpleCategoryList.as_view()),
    # url(r'^(?P<page_categories_id>\d+)/$', views.products, name='products'),
    # url(r'^(?P<page_categories_id>\d+)/(?P<page_container_id>\d+)/$', PageDetails.as_view()),
    url(r'^categories/(?P<pk>\d+)/$', CategoryListDeluxe.as_view(), name='categories'),
    url(r'^products/(?P<pk>\d+)/$', PageDetails.as_view(), name='products'),
    #
    # DetailView needs captured variable to be named "pk" as in tutorial part 4, amend views
    #
)
"""
Der Index sollte alle Kategorien "gefaltet" zeigen.
Dazu sollte es eine url mit kategorienamen als slug geben, der die jew. kategorie "ausgefaltet" zeigt.
"""
