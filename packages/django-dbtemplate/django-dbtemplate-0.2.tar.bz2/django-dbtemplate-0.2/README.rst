=================
django-dbtemplate
=================

.. image:: https://travis-ci.org/subuk/django-dbtemplate.svg?branch=master
    :target: https://travis-ci.org/subuk/django-dbtemplate
    :alt: build status


With django-dbtemplate your users may override templates from admin interface.
Main purpose of this project - allow admin users to override email templates.


Installation
------------

1. Install package

    .. code:: bash

        pip install django-dbtemplate

2. Add "dbtempalte" to INSTALLED_APPS

    .. code:: python

        INSTALLED_APPS = (
            ...
            'dbtemplate',
            ...
        )

3. Add loader "dbtemplate.loader.DatabaseLoader" to TEMPLATE_LOADERS.


For production deployments, always use `cached template loader <https://docs.djangoproject.com/en/1.8/ref/templates/api/#django.template.loaders.cached.Loader>`_ to awoid unnecessary database queries.
