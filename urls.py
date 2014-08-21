from django.conf.urls import patterns, url

from cat_nav import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page_categories_id>\d+)/$', views.page_content_view, name='content'),
)

