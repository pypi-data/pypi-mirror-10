
===========================
 django-future-staticfiles
===========================

.. image:: https://travis-ci.org/dsanders11/django-future-staticfiles.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/dsanders11/django-future-staticfiles

.. image:: https://img.shields.io/pypi/v/django-future-staticfiles.svg
   :alt: Latest PyPI version
   :target: https://pypi.python.org/pypi/django-future-staticfiles/

.. image:: https://coveralls.io/repos/dsanders11/django-future-staticfiles/badge.svg?branch=master
   :alt: Coverage
   :target: https://coveralls.io/r/dsanders11/django-future-staticfiles?branch=master

Backport of `Django`_ `staticfiles storages`_ from Django 1.7+ to earlier
Django 1.6

Overview
========

Quick and dirty backport of the latest staticfiles storages from the latest
Django to be used with Django 1.6. Tests are backported as well to ensure
everything works, but butchered to remove post-Django 1.6 tests.

Requirements
============

Requires Django 1.6+ and as such `Python`_ 2.6+ as well

Installation
============

Simply use `pip`_ to install::

    $ pip install django-future-staticfiles

Usage
=====

The storages should be drop in replacements, so they can be used in
`settings.py` for `STATICFILES_STORAGE`::

    $ STATICFILES_STORAGE='django_future_staticfiles.storage.CachedStaticFilesStorage'

Contributing
============

Contributions are welcome, just create a pull request or issue on the
`GitHub repository`_ for the project.

.. _`Django`: https://djangoproject.com/
.. _`GitHub repository`: https://github.com/dsanders11/django-migrate-project
.. _`pip`: https://pip.pypa.io/en/stable/
.. _`Python`: https://python.org/
.. _`staticfiles storages`: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#storages
