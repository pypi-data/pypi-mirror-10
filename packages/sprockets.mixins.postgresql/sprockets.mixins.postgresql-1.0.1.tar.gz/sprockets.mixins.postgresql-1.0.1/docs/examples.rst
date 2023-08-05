Examples
========
The following example demonstrates using the
:py:class:`HandlerMixin <sprockets.mixins.postgresql.HandlerMixin>` with a
synchronous Tornado :py:class:`RequestHandler <tornado.web.RequestHandler>` for a database
named ``postgres``:

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

The second example demonstrates using the
:py:class:`AsyncHandlerMixin <sprockets.mixins.postgresql.AsyncHandlerMixin>`
with an asynchronous Tornado :py:class:`RequestHandler <tornado.web.RequestHandler>`
for a database named ``foo``:

.. code:: python

    import os

    from sprockets.mixins import postgresql
    from tornado import web

    os.environ['FOO_HOST'] = 'localhost'
    os.environ['FOO_USER'] = 'postgres'
    os.environ['FOO_PORT'] = 5432
    os.environ['FOO_DBNAME'] = 'foo'
    os.environ['FOO_PASSWORD'] = 'bar'

    class FooRequestHandler(postgresql.HandlerMixin,
                            web.RequestHandler):

        DBNAME = 'foo'

        @web.asynchronous
        def get(self, *args, **kwargs):
            result = yield self.foo_session.query('SELECT * FROM baz')
            self.finish({'data': result.items()})
            result.free()

