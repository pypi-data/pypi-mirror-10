
=========================
Leonardo Redactor Wysiwyg
=========================

A lightweight wysiwyg editor for Leonardo

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo-module-redactor

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["redactor"]

Add ``leonardo_module_sentry`` to APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'leonardo_module_redactor'
        ...
    ]

    REDACTOR_OPTIONS = {
        'lang': 'en',
        'plugins': ['table', 'video', 'fullscreen', 'fontcolor', 'textdirection']}

    REDACTOR_UPLOAD = 'uploads/'

Sync static

.. code-block:: bash

    python manage.py sync_all

    # or
    
    python manage.py collectstatic --noinput



