.. _config:

Configuration Guide
===================

Database
--------

* Create tachyonic Database.
* Create user for api endpoint to access database.

The Mysql/MarioDB Schema can be found in the tachyonic_api source. https://github.com/TachyonProject/tachyonic_api/blob/development/db.sql. TODO: At some point installation can be done using other means.

**Create Database and User**

.. code:: mysql

    create database tachyonic;
    grant all on tachyonic.* to tachyonic identified by 'password';
    flush privileges;

**Load Database Schema**

.. code:: bash

    $ mysql -u tachyonic -p tachyonic < db.sql

Install API and UI
------------------

Usually applications are installed in /var/www

.. code:: bash
    
    $ sudo mkdir /var/www/tachyonic_api
    $ sudo mkdir /var/www/tachyonic_ui
    $ sudo tachyonic -s tachyonic.api /var/www/tachyonic_api
    $ sudo tachyonic -s tachyonic_ui /var/www/tachyonic_ui

settings.cfg
------------

The settings.cfg file is located within your installation directory. The purpose of this file to specify specific properties for the environment and import middleware and modules.

**API Example - /var/www/tachyonic_api/settings.cfg**

.. code::

	[application]
	name = Tachyonic API
	modules = tachyonic.api.middleware, tachyonic.api.views
	middleware = tachyonic.api.middleware.Token
	session_timeout = 7200
	use_x_forwarded_host = false
	use_x_forwarded_port = false

	[mysql]
	database = tachyonic
	host = localhost
	username = tachyonic
	password = password

	#[redis]
	#server = localhost
	#port = 6379
	#db = 0

	[logging]
	host = 127.0.0.1
	port = 514
	debug = True

	[endpoints]

	[tenants]
	driver = tachyonic.api.tenant.MysqlDriver
	create = True
	update = True

	[users]
	driver = tachyonic.api.auth.MysqlDriver
	create = True
	update = True

**UI Example - /var/www/tachyonic_ui/settings.cfg**

The *'restapi'* points to the url of the Base API above.

.. code::

	[tachyon]
	restapi = http://localhost/api

	[application]
	name = Tachyon UI
	modules = tachyonic.ui
	middleware = tachyonic.ui.middleware.Globals, tachyonic.ui.middleware.Auth
	static = /static
	session_timeout = 7200
	use_x_forwarded_host = false
	use_x_forwarded_port = false

	#[redis]
	#host = localhost
	#port = 6379
	#db = 0

	[logging]
	host = 127.0.0.1
	port = 514
	debug = True

	[tenants]
	create = True
	update = True

	[users]
	create = True
	update = True

Web Server
----------

It is assumed that you already have an understanding of configuration related to WSGI web applications.

The WSGI file to startup the API or UI is located in the application installation root under wsgi package module app.py (wsgi/app.py)

**Example Apache + mod_wsgi configuration:**

.. code::

	WSGIDaemonProcess api processes=10 threads=10 user=www group=www
	WSGIScriptAlias /api /var/www/tachyonic_api/wsgi/app.py
	<Location /api>
	WSGIProcessGroup api 
	</Location>

	WSGIDaemonProcess ui processes=10 threads=10 user=www group=www
	WSGIScriptAlias /ui /var/www/tachyonic_ui/wsgi/app.py
	Alias /static /var/www/tachyonic_ui/static
	<Location /ui>
	WSGIProcessGroup ui
	</Location>

