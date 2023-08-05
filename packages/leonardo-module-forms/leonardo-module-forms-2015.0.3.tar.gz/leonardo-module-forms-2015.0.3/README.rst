
==============
Leonardo Forms
==============

Form builder for Leonardo.

Technicaly is only FeinCMS `Form Designer`_ and `Remote Forms`_.

Visit `Demo Site`_

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo_module_forms

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["forms"]

Optionaly you can install remote forms typing this

.. code-block:: bash

    pip install leonardo_module_forms[remote]

https://github.com/WiserTogether/django-remote-forms

Add ``leonardo_module_forms`` to APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'forms'
        ...
    ]

Load new template to db

.. code-block:: bash

    python manage.py sync_all


See `Leonardo`_

.. _`Demo Site`: http://demo.cms.robotice.cz
.. _`Leonardo`: https://github.com/django-leonardo/django-leonardo
.. _`Form Designer`: https://github.com/antiflu/form_designer
.. _`Remote Forms`: https://github.com/WiserTogether/django-remote-forms
