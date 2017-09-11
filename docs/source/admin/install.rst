.. _install:

Install Guide
=============

The API endpoints can be installed on seperate servers including having dedicated servers for UI / Web Application frontend. 

Redis is used for sharing session data for web application when deployed on multiple servers. However when using a single server a directory can be used for session files.

Requirements
------------

* Web Server for loading WSGI application.
* MySQL or MariaDB Database Server. (Cluster or replication recommended for redundancy)
* Redis (optional when using multiple web servers for GUI)

Using Packages
--------------

*Please note packages are not currently on pypi. Once first stable branch is releaed the packages will be submitted! Use the source below for installation from development branch!*

**Install the following components:**

.. code:: bash

    $ pip install tachyonic.common
    $ pip install tachyonic.neutrino
    $ pip install tachyonic.client
    $ pip install tachyonic.api
    $ pip install tachyonic.ui

**or alternatively:**

.. code:: bash

    $ pip install tachyonic

    
Using Source
------------

**Clone source code into a directory for tachyonic.**

.. code:: bash

    $ git clone -b development clone https://github.com/TachyonProject/tachyonic_common.git
    $ git clone -b development clone https://github.com/TachyonProject/tachyonic_neutrino.git
    $ git clone -b development clone https://github.com/TachyonProject/tachyonic_client.git
    $ git clone -b development clone https://github.com/TachyonProject/tachyonic_api.git
    $ git clone -b development clone https://github.com/TachyonProject/tachyonic_ui.git

**Installing source code:**

.. code:: bash

    $ pip install tachyonic_common
    $ pip install tachyonic_neutrino
    $ pip install tachyonic_client
    $ pip install tachyonic_api
    $ pip install tachyonic_ui

Or, if you want to edit the code, first fork the main repo, clone the fork
to your desktop, and then run the following to install it using symbolic
linking, so that when you change your code, the changes will be automagically
available to your app without having to reinstall the package:

.. code:: bash

    $ pip -e install tachyonic_common
    $ pip -e install tachyonic_neutrino
    $ pip -e install tachyonic_client
    $ pip -e install tachyonic_api
    $ pip -e install tachyonic_ui

