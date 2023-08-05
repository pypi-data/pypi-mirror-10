=======================
django-storages-folder
=======================

About
=====
django-storage-folder is a small extension to the django-storages-redux_ (a
python3 compatible fork of django-storages) project that allows you to specify
different directories for storing media and static files.

It currently only supports the s3boto backend.

.. _django-storages-redux: https://pypi.python.org/pypi/django-storages-redux/

How To Use
==========

#. Set the static files or media files storage backend

#. Set the static files or media files storage directory

..

    STATICFILES_STORAGE = 'storages_folder.backends.s3boto.StaticStorage'
    STATICFILES_STORAGE_DIR = 'static'

    MEDIAFILES_STORAGE = 'storages_folder.backends.s3boto.MediaStorage'
    MEDIAFILES_STORAGE_DIR = 'media'
