from django.db import models

# achtung, könnte verkehrt aufgegleist sein. mir ist nicht klar, ob sich kategorien auf seiteninhalte beziehen müssen oder umgekehrt. verglichen mit dem 'Polls' Beispiel ...

class product_categories(models.Model):
    category_name = models.CharField(max-length=100)
    category_order = models.IntegerField(default=0)
    def __unicode__(self):
        return self.question

class page_container(models.Model):
    # Content of page and it's title. What max_length should be used here?
    page_title = models.CharField(max_length=200)
    page_content = models.CharField(max_length=1200)
    # Number to be used to define order of listed page names
    page_order = models.IntegerField(default=0)
    # Category ("~ies"?)
    page_categories = models.ManyToManyField(product_categories)
    # Links to Pages containing similar Information
    page_context_links = models.XXXXXXXX()
    def __unicode__(self):
        return self.question
