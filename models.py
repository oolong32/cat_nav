# -*- coding: utf-8 -*-
from django.db import models

# achtung, könnte verkehrt aufgegleist sein. mir ist nicht klar, ob sich kategorien auf seiteninhalte beziehen müssen oder umgekehrt. verglichen mit dem 'Polls' Beispiel ...
# Ebenfalls unklar: Ist die Beziehung Pages-Categories eine "one to many" oder eine "many to many" beziehung?

class product_categories(models.Model):
    category_name = models.CharField(max_length=100)
    # Should eventually allow the admin to change the order by which the categories are displayed
    category_order = models.IntegerField(default=0)
    def __unicode__(self):
        return self.category_name

class page_container(models.Model):
    # Content of page and it's title. What max_length should be used here?
    page_title = models.CharField(max_length=200)
    # TextField Info: https://docs.djangoproject.com/en/1.6/ref/models/fields/#django.db.models.TextField
    page_content = models.TextField(max_length=1200)
    # Number to be used to define order of listed page names
    page_order = models.IntegerField(default=0)
    # Category ("~ies"?)
    page_categories = models.ForeignKey(product_categories)
    # Links to Pages containing similar Information
    """
    Der nächste Punkt soll Links zu Seiten enthalten, die verwandte Produkte enthalten. Voraussichtlich ist hier der falsche Ort dafür. Ich gehe davon aus, dass es hierfür eine eigene Klasse brauchen wird.
    """
    # page_context_links = models.XXXXXXXX()
    
    """
    In Python 3 __unicode__ will need to be replaced by __str__ (?)
    """
    def __unicode__(self):
        """
        return self.page_title
        return self.page_content
