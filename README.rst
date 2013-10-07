===========
GDG DevFest
===========

DevFest website for all italian GDGs

* Free software: BSD license

Requirements
------------

* Django 1.5+
* Python 2.7
* `django-cms`_ 3.0.0.beta2

.. _django-cms: https://github.com/divio/django-cms/tree/3.0.0.beta2

Installation
------------

Enter inside ``django-devfest`` folder and install all requirements inside a virtualenv:

.. code-block:: python

    pip install -r requirements/development.txt

Enter inside ``django_cms`` then prepare your database (sqlite as default) and run the server:

.. code-block:: python

    python manage.py syncdb --all --settings=django_cms.settings.dev
    python manage.py migrate --fake --settings=django_cms.settings.dev
    python manage.py cms check --settings=django_cms.settings.dev
    python manage.py runserver --settings=django_cms.settings.dev

Create your first page with Django CMS admin (``http://localhost:8000``)!

Features
--------

* DevFest homepage is fully customizable with a default stock template

Credits
-------

Thanks to `GDG Fresno`_ for this template. Original template is available on GDG-X `repository`_.

.. _GDG Fresno: http://gdgfresno.com
.. _repository: https://github.com/gdg-x/devfest-template
