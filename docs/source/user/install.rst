.. _install:

Installation
============

A package is availible on PyPI for the Tachyonic framework.
Installing it is as simple as:

.. code:: bash

    $ pip install tachyonic

Dependencies
------------
Tachyonic depends on:

.. include:: ../../requirements.txt

Ubuntu Notes
~~~~~~~~~~~~
Before running pip install tachyonic you may be required to install some distribution packages required.

.. code:: bash

    $ apt-get install libffi-dev
    $ apt-get install libmysqlclient-dev

WSGI Server
-----------
Tachyonic speaks WSGI, and so in order to serve a Tachyonic application, you will need a WSGI Server. Tested working with apache2 and mod_wsgi.

On Ubuntu the package is known as: libapache2-mod-wsgi

**Please note libapache2-mod-wsgi-py3 is for Python 3 and we only support 2.7 at this time.**


Source Code
-----------
Tachyonic infrastructure and code is hosted on `GitHub <https://github.com/TachyonProject/tachyonic>`_. Making the code easy to browse, download, fork, etc. Pull requests are always welcome!

Clone the project like this:

.. code:: bash

	$ git clone https://github.com/TachyonProject/tachyonic.git

Once you have cloned the repo or downloaded a tarball from GitHub, you
can install Tachyonic like this:

.. code:: bash

    $ cd tachyonic
    $ pip install .

Or, if you want to edit the code, first fork the main repo, clone the fork
to your desktop, and then run the following to install it using symbolic
linking, so that when you change your code, the changes will be automagically
available to your app without having to reinstall the package:

.. code:: bash

    $ cd tachyonic
    $ pip install -e .

You can manually test changes to the Neutrino framework by switching to the
directory of the cloned repo:

.. code:: bash

    $ pip install requirements-dev.txt
    $ tox
