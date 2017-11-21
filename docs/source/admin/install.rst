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

    $ sudo pip install tachyonic.common
    $ sudo pip install tachyonic.neutrino
    $ sudo pip install tachyonic.client
    $ sudo pip install tachyonic.api
    $ sudo pip install tachyonic.ui

**or alternatively:**

.. code:: bash

    $ pip install tachyonic

    
Using Source
------------

**Clone source code into a directory for tachyonic.**

.. code:: bash

    $ git clone -b development https://github.com/TachyonProject/tachyonic_common.git
    $ git clone -b development https://github.com/TachyonProject/tachyonic_neutrino.git
    $ git clone -b development https://github.com/TachyonProject/tachyonic_client.git
    $ git clone -b development https://github.com/TachyonProject/tachyonic_api.git
    $ git clone -b development https://github.com/TachyonProject/tachyonic_ui.git

**Installing source code:**

.. code:: bash

    $ cd tachyonic_common
    $ sudo pip install .
    $ cd ../tachyonic_neutrino
    $ sudo pip install .
    $ cd ../tachyonic_client
    $ sudo pip install .
    $ cd ../tachyonic_api
    $ sudo pip install .
    $ cd ../tachyonic_ui
    $ sudo pip install .

Or, if you want to edit the code, first fork the main repo, clone the fork
to your desktop, and then run the following to install it using symbolic
linking, so that when you change your code, the changes will be automagically
available to your app without having to reinstall the package:

.. code:: bash

    $ cd tachyonic_common
    $ sudo pip install -e .
    $ cd ../tachyonic_neutrino
    $ sudo pip install -e .
    $ cd ../tachyonic_client
    $ sudo pip install -e .
    $ cd ../tachyonic_api
    $ usod pip install -e .
    $ cd ../tachyonic_ui
    $ sudo pip install -e .


Using Docker
------------

Docker is a quick way to get the latest Tachyonic up and running with no hassle.
If you have downloaded and installed Docker, simply copy `this Dockerfile
<https://raw.githubusercontent.com/TachyonicProject/tachyonic_ui/development/tachyonic/ui/resources/Dockerfile>`_ to any
directory, and from that directory first build your image with:

.. code:: bash

    $ docker build -t tachyonic .

Next run the container, taking note of the port on which you want it to be served.

.. code:: bash

    $ docker run -it -p 80:80 tachyonic

Simply point your browser to http://localhost/ui to get a feel for the base Tachyonic installation.

