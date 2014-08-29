#App to Publish Categorized Information

##What is needed

In order to build a webpage with a category based navigation the following is needed:

###Check

* Add one[&sup1;](#1) category to a _page_
* List these categories
* List names of pages for each category
* Dropdown list of existing categories in admin interface of page (or radio buttons?)
* Possibility of creating new category
* Possibility of changing page's category at a later time
* Impossibility of publishing without choosing a category
* Possibilty to define/change order of category list view
* Possibilty to define/change order of page list view
* Possibility to add links to other pages at the end of a page's content

###To Do

* Possibilty of choosing "context links" for a given product page[&sup2;](#2)
* Retrieve Information from Link/URL to write HTML class
* Markdown editor for page content
* Front-end design

###Obsolete/doesn't matter

* What is the default category for a page? Needs to be set, otherwise an error will be raised or other kinds of trouble might arise



##Addendum

###<a name="1"></a>1)
At a later time the neccessity of being able to add more than one cateogory to a page might arise.

Or it might not.

###<a name="2"></a>2)
When editing the detail information for a given product, the user should be able to choose a couple of entries from a list of all existing products. Links to these product's detail pages should then be displayed at the bottom of a product's detail page once published.

##Tests

There should be tests for:

* Whether a page has a category
* What happens with pages that have a category that is deleted?

It seems these tests aren't neccessary at all. Django doesn't allow a page without category and deletes pages, when their category is deleted (not without asking first, of course).

##Installation/Set Up

I try to record all neccessary changes to files outside of the app (this repo). _project_folder_ needs to be changed to the respective project's name.

###Changes to ../project_folder/settings.py

Edit the mysite/settings.py file again, and change the INSTALLED_APPS setting to include the string 'cat_nav'. 

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cat_nav',
)
```

Then create the neccessary tables in the database:

`$ python manage.py sql cat_nav`

You should see something similar to the following (the CREATE TABLE SQL statements for the cat_nav app):

```sql
BEGIN;
CREATE TABLE "cat_nav_product_categories" (
    "id" integer NOT NULL PRIMARY KEY,
    "category_name" varchar(100) NOT NULL,
    "category_order" integer NOT NULL
)
;
CREATE TABLE "cat_nav_page_container" (
    "id" integer NOT NULL PRIMARY KEY,
    "page_title" varchar(200) NOT NULL,
    "page_content" text NOT NULL,
    "page_order" integer NOT NULL,
    "page_categories_id" integer NOT NULL REFERENCES "cat_nav_product_categories" ("id")
)
;

COMMIT;
```

Now, run syncdb again to create those model tables in your database:

> $ python manage.py syncdb

###Changes to and ../project_folder/urls.py

Point the root URLconf at the cat_nav.urls module. In project_folder/urls.py insert an include().

```python
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^cat_nav/', include('cat_nav.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
```


###Changes to files in ../templates/admin/

Open your settings file (project_folder/settings.py) and add a TEMPLATE_DIRS setting:

```python
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
```

Copy the template admin/base_site.html from within the default Django admin template directory in the source code of Django itself (django/contrib/admin/templates) into that directory.
Hint: Django resides (in my case) in python's 'site-packages' folder.

Edit as you see fit.

##Tests in the Python Interpreter

So far, with a model configuration that is based on the django poll tutorial, whereas I replaced the "Poll" model with _product_categories_ and "Choices" with _page_containers_, I can create pages that refer to _one_ category. And categories that refer to multiple pages. I am not sure however, whether it's possible to have pages, that belong to _more than one category_.
Update: Indeed, it is not possible. Django handles everything most gracefully however. Maybe it will suffice like it is.

```python
>>> p = product_categories.objects.get(pk=1)
>>> p
<product_categories: hunde>
>>> p.page_container_set.all()
[]
>>> p.page_container_set.create(page_title="dackel", page_content="dackel sind klein und lang.")
<page_container: dackel>
>>> p.page_container_set.create(page_title="mops", page_content="möpse sind klein, kurz und haben eine flache schnauze.")
<page_container: mops>
>>> c = p.page_container_set.create(page_title="terrier", page_content="im gegensatz
 zu dackeln und möpsen sind terrier schon eher als richtige hunde zu bezeichnen.")
>>> c.page_categories
<product_categories: hunde>
>>> p.page_container_set.all()
[<page_container: dackel>, <page_container: mops>, <page_container: terrier>]
>>> p.page_container_set.count()
3
```
