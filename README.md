#App to Publish Categorized Information

##What is needed

In order to build a webpage with a three-column layout, whereas the first two columns contain a list of categories and a list of pages respectively while the third column contains the "page", the following is needed:

* Add one[&sup1;](#one) category to a _page_
* List these categories
* List names of pages for each category
* Dropdown list of existing categories in admin interface of page (or radio buttons?)
* Possibility of creating new category
* Possibility of changing page's category at a later time
* Impossibility of publishing without choosing a category
* Possibilty to define/change order of category list view
* Possibilty to define/change order of page list view
* Markdown editor for page content
* Possibility to add links to other pages at the end of a page's content




##Addendum

###<a name="one"></a>1)

At a later time the neccessity of being able to add more than one cateogory to a page might arise.

##Tests

There should be tests for:

* Wether a page has a category
* What happens with pages that have a category that is deleted?

##Documentation

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

> $ python manage.py sql cat_nav

You should see something similar to the following (the CREATE TABLE SQL statements for the cat_nav app):

```shell
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

###Changes to ../project_folder/urls.py

###Chagens to files in ../templates/admin/

