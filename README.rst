=======================
djangocms-scroll-smooth
=======================

------------

Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`, run ``pip install djangocms-scroll-smooth``
* If using Django 1.6 add ``'djangocms_wow': 'djangocms_scroll_smooth.south_migrations',``
  to ``SOUTH_MIGRATION_MODULES``  (or define ``SOUTH_MIGRATION_MODULES`` if it does not exists);
* Run ``manage.py migrate djangocms_scroll_smooth``


Usage
-----

Default content in Placeholder
******************************

If you use Django-CMS >= 3.0, you can use ``Smooth Scroll`` in "default_plugins"
(see docs about the CMS_PLACEHOLDER_CONF setting in Django CMS 3.0).
