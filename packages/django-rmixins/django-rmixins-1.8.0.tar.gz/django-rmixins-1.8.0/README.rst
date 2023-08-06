==========================
django-rmixins
==========================

What is it?
===========

django-rmixins is a simple Django App that contains some Mixins to use for
Django's Class Based Views.

Installation
============

You can do any of the following to install ``django-rmixins``

- Run ``pip install django-rmixins``.
- Run ``easy_install django-rmixins``.
- Download or "hg clone" the package and run ``setup.py``.
- Download or "hg clone" the package and add ``rmixins`` to your PYTHONPATH.

Usage
=====

For example if you'd like to use the ``CacheMixin``::

    from django.views.generic import ListView

    from rmixins.mixins import CacheMixin

    class PostsListView(CacheMixin, ListView):
        cache_timeout = 900
        model = Posts
