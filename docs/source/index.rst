.. Tachyonic documentation master file, created by
   sphinx-quickstart on Sat Mar 18 07:45:34 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Tachyonic's documentation!
=====================================

Release v\ |version| (:ref:`Installation <install>`)

Tachyonic is a flexible Python Web and RestApi application framework for rapid development.
It's free and open source and before you ask:
It's BSD Licensed!

Contributions and contributors are welcome!

.. code:: python

    class Books(tachyonic.Resource):
        def __init__(self, app):
            app.router.add(tachyonic.HTTP_GET, '/books/{id}', self.view_book)

        def view_book(self, req, resp, id):
            resp.headers['Content-Type'] = nfw.TEXT_HTML
            title, book = book(id)
            t = tachyonic.jinja.get_template('myproject/view_book.html')
            resp.body = t.render(title=title, book=book)

Features
--------

- Routes based on URI templates.
- Jinja2 templating integration.
- Simple ORM. (serialized data json import and export)
- Mariadb/Mysql Pool manager and simple interface
- Policy/Rules Engine - Access control to resources.
- Logging Facilities.
- Loading of resource classes via configuration file.

Useful Links
------------

- `Tachyonic Home <http://tachyonic.co.za/>`_
- Tachyonic @ PyPI - Coming Soon
- `Tachyonic @ GitHub <https://github.com/TachyonProject/tachyonic>`_

Documentation
-------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   user/index
   api/index
   community/index
