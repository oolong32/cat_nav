from django.conf.urls import patterns, url

from cat_nav.views import CategoryList
from cat_nav import views

urlpatterns = patterns('',
    url(r'^$', CategoryList.as_view()),
    # url(r'^(?P<page_categories_id>\d+)/$', views.products, name='products'),
    url(r'^(?P<page_categories_id>\d+)/details/(?P<page_container_id>\d+)/$', views.details, name='details'),
)
"""
Im Tutorial wird unter #4 gezeigt, wie "generic Views" gehen. Habe ich nicht begriffen. - ev. noch nachschlagen und einrichten.
https://docs.djangoproject.com/en/1.6/topics/class-based-views/
"""
