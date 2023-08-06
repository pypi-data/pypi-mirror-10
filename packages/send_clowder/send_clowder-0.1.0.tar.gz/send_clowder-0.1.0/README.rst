===============================
send_clower
===============================

.. image:: https://img.shields.io/travis/etscrivner/send_clowder.svg
        :target: https://travis-ci.org/etscrivner/send_clowder

.. image:: https://img.shields.io/pypi/v/send_clowder.svg
        :target: https://pypi.python.org/pypi/send_clowder

Simple command-line tool for sending messages to clowder.io.

* Free software: BSD license
* Documentation: https://send_clowder.readthedocs.org.

Installation
------------

Simply install the application from PyPI.

.. code-block:: shell

   pip install send_clowder

Usage
-----

To send an ok status update simply pipe your values as follows:

.. code-block:: shell

   echo -e "25" | xargs send_clowder APIKEY ok my_service -v

To send a failure status simply change ok to fail:

.. code-block:: shell

   echo -e "25" | xargs send_clowder APIKEY fail my_service -v
