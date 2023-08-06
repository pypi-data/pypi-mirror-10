
==================================
Awesome Galleries for Leonardo CMS
==================================

New galleries for Leonardo CMS.

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo-gallery

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["gallery"]

Add ``gallery`` to APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'leonardo_gallery'
        ...
    ]

Run management commands

.. code-block:: bash

    python manage.py sync_all

    # or
    
    python manage.py collectstatic --noinput

Read More
---------

* https://github.com/django-leonardo/django-leonardo
* http://leonardo.robotice.org

