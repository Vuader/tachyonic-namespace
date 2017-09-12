=========
Tachyonic
=========

.. image:: https://travis-ci.org/TachyonProject/tachyonic.svg?branch=master
    :target: https://travis-ci.org/TachyonProject/tachyonic
    :alt: Build Status

.. image:: https://readthedocs.org/projects/tachyonic/badge/?version=latest
    :target: http://tachyonic.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
    
.. image:: https://badge.waffle.io/TachyonProject/tachyonic.png?label=ready&title=Ready 
    :target: https://waffle.io/TachyonProject/tachyonic 
    :alt: 'Stories in Ready'

Quick Links
-----------

* `Website <http://tachyonic.co.za>`__.
* `Documentation <http://tachyonic.readthedocs.io>`__.

Installation
------------

Tachyon currently fully supports `CPython <https://www.python.org/downloads/>`__ 2.7.

Source Code
-----------

Tachyon infrastructure and code is hosted on `GitHub <https://github.com/TachyonProject/tachyonic>`_.
Making the code easy to browse, download, fork, etc. Pull requests are always welcome!

Clone the project like this:

.. code:: bash

    $ git clone https://github.com/TachyonProject/tachyonic.git

Once you have cloned the repo or downloaded a tarball from GitHub, you
can install Tachyon like this:

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

You can manually test changes to the tachyonic by switching to the
directory of the cloned repo:

.. code:: bash

    $ pip install -r requirements-dev.txt
    $ tox
