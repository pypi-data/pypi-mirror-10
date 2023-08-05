Welcome to django-bootstrap-ui
==============================

.. image:: https://img.shields.io/travis/timorieber/django-bootstrap-ui.svg
    :target: https://travis-ci.org/timorieber/django-bootstrap-ui

.. image:: https://img.shields.io/coveralls/timorieber/django-bootstrap-ui/master.svg
    :target: https://coveralls.io/r/timorieber/django-bootstrap-ui?branch=master

.. image:: https://img.shields.io/pypi/v/django-bootstrap-ui.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-ui

.. image:: https://img.shields.io/pypi/l/django-bootstrap-ui.svg
    :target: http://en.wikipedia.org/wiki/ISC_license

.. image:: https://readthedocs.org/projects/django-bootstrap-ui/badge/
    :target: https://django-bootstrap-ui.readthedocs.org

django-bootstrap-ui aims to be a powerful Django app to ease the integration of the popular `Bootstrap UI framework`_. It is written in `Python`_ and built on the `Django web framework <https://www.djangoproject.com/>`_.

The code is open source, and available on `GitHub`_.

.. _Bootstrap UI framework: http://getbootstrap.com/
.. _Python: https://www.python.org/
.. _Django web framework: https://www.djangoproject.com/
.. _GitHub: https://github.com/timorieber/django-bootstrap-ui

Getting started
---------------

#. First install the package using ``pip`` with the ``--pre`` option as long as this is a pre-release::

    pip install --pre django-bootstrap-ui

#. Add ``bootstrap_ui`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'bootstrap_ui',
        ...
    )

#. Load ``bootstrap_ui_tags`` in your template::

    {% load bootstrap_ui_tags %}

#. Use bootstrap components through intuitive template tags::

    {% listgroup %}
        {% listgroupitem %}
            Your raw text.
        {% endlistgroupitem %}
        {% listgroupitem %}
            You may also use a {{ context_variable }}.
        {% endlistgroupitem %}
    {% endlistgroup %}

#. Some bootstrap components support different html tags, to change the default add a parameter::

    {% listgroup use_tag="div" %}
        ...
        Your list group content goes here.
        ...
    {% endlistgroup %}

Available bootstrap components
------------------------------

* List group (http://getbootstrap.com/components/#list-group)
* Panels (http://getbootstrap.com/components/#panels)


