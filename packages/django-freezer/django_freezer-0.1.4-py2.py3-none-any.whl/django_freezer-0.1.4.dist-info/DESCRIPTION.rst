==============
django-freezer
==============
.. image:: https://travis-ci.org/inirudebwoy/django-freezer.svg?branch=master
   :target: https://travis-ci.org/inirudebwoy/django-freezer

Code can be found here.
https://github.com/inirudebwoy/django-freezer

Docs.
http://django-freezer.readthedocs.org

Installation
============
Install from pip::

  pip install django-freezer

Put package in INSTALLED_APPS.::

  INSTALLED_APPS += ('django_freezer',)

In urls.py add import of AdminSiteExtended from djangofreezer::

  from django_freezer.admin import AdminSiteExtended

Next create new extended site before calling autodiscover()::

  admin.site = AdminSiteExtended()

If you are using Django 1.7 and higher than it is necessery to disable autodiscover
as per `manual <https://docs.djangoproject.com/en/1.7/ref/contrib/admin/#django.contrib.admin.autodiscover>`_

Running unit tests
==================
Just use tox::
  $ tox


