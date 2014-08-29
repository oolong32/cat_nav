from django.conf.urls import patterns, url

from cat_nav.views import CategoryList
from cat_nav import views

urlpatterns = patterns('',
    url(r'^$', CategoryList.as_view()),
    # url(r'^(?P<page_categories_id>\d+)/$', views.products, name='products'),
    url(r'^(?P<page_categories_id>\d+)/details/(?P<page_container_id>\d+)/$', views.details, name='details'),
)
"""
<page_categories_id> muss durch lesbare namen ersetzt werden. durch den "category_name hinter der page_categories_id.
genauso sollte die referenz zum page_container objekt nicht durch eine id, sondern durch den namen angezeigt werden.
dem aufmerksamen betrachter mag aufgefallen sein, dass die url fuer "details" fehlerhaft ist, es gibt keine referenz zu einem objekt in "page_container"
Was passiert mit Bezeichnungen, die Underscores oder Spaces enthalten?

Im Produkt Template gibt es immer noch einen hard-coded Link - keine ahnung, wie ich den vereinfachen kann, weil er an zwei unterschiedlichen Stellen einen Wert "einfaengt".

Im Tutorial wird unter #4 gezeigt, wie "generic Views" gehen. Habe ich nicht begriffen. - ev. noch nachschlagen und einrichten.
https://docs.djangoproject.com/en/1.6/topics/class-based-views/


"""
