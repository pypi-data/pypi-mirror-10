sprockets.handlers.status
=========================
A small handler for reporting application status

|Version| |Downloads| |Status| |Coverage| |License|

Installation
------------
``sprockets.handlers.status`` is available on the
`Python Package Index <https://pypi.python.org/pypi/sprockets.handlers.status>`_
and can be installed via ``pip`` or ``easy_install``:

.. code:: bash

  pip install sprockets.handlers.status

Documentation
-------------
https://sprocketshandlersstatus.readthedocs.org

Example
-------
The following example demonstrates how to initialize the status handler for the
base application status page.

.. code:: python

    import tornado.ioloop
    import tornado.web
    from sprockets.handlers import status


    application = tornado.web.Application([
        ('/status', status.StatusHandler),
    ])

    if __name__ == '__main__':

        # Set the application name to the local package
        status.set_application('mypackage')

        application.listen(8888)
        tornado.ioloop.IOLoop.current().start()

Version History
---------------
Available at https://sprocketshandlersstatus.readthedocs.org/en/latest/history.html

.. |Version| image:: https://img.shields.io/pypi/v/sprockets.handlers.status.svg?
   :target: http://badge.fury.io/py/sprockets.handlers.status

.. |Status| image:: https://img.shields.io/travis/sprockets/sprockets.handlers.status.svg?
   :target: https://travis-ci.org/sprockets/sprockets.handlers.status

.. |Coverage| image:: https://img.shields.io/codecov/c/github/sprockets/sprockets.handlers.status.svg?
   :target: https://codecov.io/github/sprockets/sprockets.handlers.status?branch=master

.. |Downloads| image:: https://img.shields.io/pypi/dm/sprockets.handlers.status.svg?
   :target: https://pypi.python.org/pypi/sprockets.handlers.status

.. |License| image:: https://img.shields.io/pypi/l/sprockets.handlers.status.svg?
   :target: https://sprockets.handlers.status.readthedocs.org
