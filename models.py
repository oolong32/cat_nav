# -*- coding: utf-8 -*-
from django.db import models

class product_categories(models.Model):
    category_name = models.CharField(max_length=100)
    category_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.category_name

    class Meta:
        ordering = ["category_order"]

class page_container(models.Model):
    page_title = models.CharField('Title', max_length=200)
    page_content = models.TextField('Content', max_length=1200)
    page_order = models.IntegerField('Order of Page', default=0)
    page_categories = models.ForeignKey(product_categories, verbose_name="Category")
    page_context_links = models.ManyToManyField('self', blank=True, symmetrical=False)
    
    """
    In Python 3 __unicode__ will need to be replaced by __str__ (?)
    """

    def __unicode__(self):
        return self.page_title
        return self.page_content
    
    class Meta:
        ordering = ["page_order"]
