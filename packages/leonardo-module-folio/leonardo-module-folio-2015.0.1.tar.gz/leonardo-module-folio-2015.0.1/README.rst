
==============
Leonardo Folio
==============

Folio model and widgets for Leonardo

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo_module_folio

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["folio"]

Add ``leonardo_module_folio`` to APPS list, in the ``local_settings.py``::

    APPS = [
    	...
        'leonardo_module_folio'
    	...
    ]

Load new template to db

.. code-block:: bash

	python manage.py sync_all
