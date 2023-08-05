.. image:: https://api.travis-ci.org/danfairs/django-lazysignup.png

Introduction
============

``django-lazysignup-redux`` is a fork of ``django-lazysignup`` that supports
Django 1.7 and 1.8 until
https://github.com/danfairs/django-lazysignup/pull/44 is merged and released.


``django-lazysignup`` is a package designed to allow users to interact with a
site as if they were authenticated users, but without signing up. At any time,
they can convert their temporary user account to a real user account.

`Read the full documentation`_.

.. _Read the full documentation: http://django-lazysignup.readthedocs.org/

Tests
=====

To run the tests, do the following::

python manage.py test
