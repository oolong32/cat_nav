from django.conf.urls import patterns, url 
from cat_nav.views import SimpleCategoryList, CategoryListDeluxe, PageDetails
from cat_nav import views

urlpatterns = patterns('',
    url(r'^$', SimpleCategoryList.as_view()),
    url(r'^categories/(?P<pk>\d+)/$', CategoryListDeluxe.as_view(), name='categories'),
    url(r'^products/(?P<pk>\d+)/$', PageDetails.as_view(), name='products'),
)
