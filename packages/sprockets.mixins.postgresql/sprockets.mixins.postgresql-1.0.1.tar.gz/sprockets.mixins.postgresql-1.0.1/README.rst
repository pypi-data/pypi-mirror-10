sprockets.mixins.postgresql
===========================
Handler mixins that automatically connect a PostgreSQL client session upon initialization.

|Version| |Downloads| |Status| |Coverage| |License|

Installation
------------
sprockets.mixins.postgresql is available on the
`Python Package Index <https://pypi.python.org/pypi/sprockets.mixins.postgresql>`_
and can be installed via ``pip`` or ``easy_install``:

.. code:: bash

  pip install sprockets.mixins.postgresql

Documentation
-------------
https://sprocketsmixinspostgresql.readthedocs.org

Requirements
------------
-  `sprockets <https://github.com/sprockets/sprockets>`_
-  `sprockets.clients.postgresql <https://github.com/sprockets/sprockets.clients.postgresql>`_

Example
-------
The following example demonstrates using the ``HandlerMixin`` with a
synchronous Tornado ``RequestHandler <tornado.web.RequestHandler>`` for a
database named ``postgres``:

.. code:: python

    import os

    from sprockets.mixins import postgresql
    from tornado import web

    os.environ['POSTGRES_HOST'] = 'localhost'
    os.environ['POSTGRES_USER'] = 'postgres'
    os.environ['POSTGRES_PORT'] = 5432
    os.environ['POSTGRES_DBNAME'] = 'postgres'

    class PostgresRequestHandler(postgresql.HandlerMixin,
                                 web.RequestHandler):

        DBNAME = 'postgres'

        def get(self, *args, **kwargs):
            result = self.foo_session.query('SELECT * FROM bar')
            self.finish({'data': result.items()})

The second example demonstrates using the ``AsyncHandlerMixin`` with an
asynchronous Tornado ``RequestHandler`` for a database named ``foo``:

.. code:: python

    import os

    from sprockets.mixins import postgresql
    from tornado import web

    os.environ['FOO_HOST'] = 'localhost'
    os.environ['FOO_USER'] = 'postgres'
    os.environ['FOO_PORT'] = 5432
    os.environ['FOO_DBNAME'] = 'foo'
    os.environ['FOO_PASSWORD'] = 'bar'

    class FooRequestHandler(postgresql.AsyncHandlerMixin,
                            web.RequestHandler):

        DBNAME = 'foo'

        @web.asynchronous
        def get(self, *args, **kwargs):
            result = yield self.foo_session.query('SELECT * FROM baz')
            self.finish({'data': result.items()})
            result.free()

Version History
---------------
Available at https://sprocketsmixinspostgresql.readthedocs.org/en/latest/history.html

.. |Version| image:: https://badge.fury.io/py/sprockets.mixins.postgresql.svg?
   :target: http://badge.fury.io/py/sprockets.mixins.postgresql

.. |Status| image:: https://travis-ci.org/sprockets/sprockets.mixins.postgresql.svg?branch=master
   :target: https://travis-ci.org/sprockets/sprockets.mixins.postgresql

.. |Coverage| image:: https://img.shields.io/coveralls/sprockets/sprockets.mixins.postgresql.svg?
   :target: https://coveralls.io/r/sprockets/sprockets.mixins.postgresql

.. |Downloads| image:: https://pypip.in/d/sprockets.mixins.postgresql/badge.svg?
   :target: https://pypi.python.org/pypi/sprockets.mixins.postgresql

.. |License| image:: https://pypip.in/license/sprockets.mixins.postgresql/badge.svg?
   :target: https://sprocketsmixinspostgresql.readthedocs.org
