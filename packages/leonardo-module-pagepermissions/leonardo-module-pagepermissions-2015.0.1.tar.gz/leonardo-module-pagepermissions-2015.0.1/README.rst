
=========================
Leonardo Page Permissions
=========================

Leonardo Page Permissions based on https://github.com/ebrelsford/feincms-pagepermissions

This plugin extends Leonardo Page and provide new Navigation templates which repsect your permissions.

*Check whether the user has permission to view the page. If the user has any of the page's permissions, they have permission. If the page has no set permissions, they have permission.*

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo_module_pagepermissions

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["pagepermissions"]

Add ``leonardo_module_sentry`` to APPS list, in the ``local_settings.py``::

    APPS = [
    	...
        'leonardo_module_pagepermissions'
        ...
    ]

Load new template to db

.. code-block:: bash

	python manage.py sync_all

Read more
---------

* https://github.com/ebrelsford/feincms-pagepermissions