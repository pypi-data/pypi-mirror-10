
================
Team Application
================

A lightweight Team Application for Leonardo CMS and FeinCMS

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo-team

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["team"]

Add ``team`` to APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'team'
        ...
    ]

Run management commands

.. code-block:: bash

    python manage.py makemigrations --noinput
    python manage.py migrate --noinput

    python manage.py sync_all

    # or
    
    python manage.py collectstatic --noinput

Read More
---------

* https://github.com/django-leonardo/django-leonardo
* leonardo.robotice.org

