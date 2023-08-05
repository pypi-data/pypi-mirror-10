Official Picnic API client library for Python
=============================================

A Python library for Picnic's API. Only Python 3 is supported.

Setup
-----

You can install this package—and its one dependency, ``requests``—by doing::

    pip install picnic-python

or::

    easy_install picnic-python

Obtaining a Picnic API Key
--------------------------

Sign up for an API key at https://picnic.sh/api.

Using the Picnic API
--------------------

Documentation for the API can be found at https://picnic.sh/api.

Using this client library
-------------------------

For a quick demonstration of the available methods, please see `example.py`_.

.. _example.py: example.py

list_websites()
^^^^^^^^^^^^^^^

Returns a list of ``Website`` s that you own.

get_website(*domain_name*)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a ``Website`` referred to by the given *domain_name*.

get_price(*domain_name*)
^^^^^^^^^^^^^^^^^^^^^^^^

Returns a ``DomainStatus`` for the given *domain_name*.

create_website(*domain_name*, *html*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a website with the given *html* content at the given *domain_name*, if available. If successful, returns a ``Website``.

Website.update_content(*html*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Overwrites the ``Website``'s content with the given *html*.

