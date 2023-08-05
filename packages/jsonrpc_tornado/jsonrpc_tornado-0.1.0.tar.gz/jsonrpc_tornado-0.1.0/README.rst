jsonrpc_tornado: a compact asynchronous JSON-RPC client library for `Tornado framework <http://www.tornadoweb.org/>`_
=======================================================================================================

Main Features
-------------

* Python 2.7 & 3.4 compatible
* Exposes tornado.httpclient options
* Non-Blocking I/O
* Supports nested namespaces (eg. `app.users.getUsers()`)

Install
-------
pip install git+https://github.com/artemmus/jsonrpc_tornado.git

Usage
-----
A synchronous example:

.. code-block:: python

    from jsonrpc_tornado import JSONRPCServer
    from tornado.httpclient import HTTPClient

    def fetch(server_url):
        server = JSONRPCServer(server_url, http_client=HTTPClient, 
            request_timeout=5.0)

        # call some function on the server
        result = server.foo(1, 2)


An example of non-blocking calls:

.. code-block:: python

    from jsonrpc_tornado import JSONRPCServer, ProtocolError, TransportError
    from tornado import gen

    @gen.coroutine
    def fetch_coroutine(server_url):
        server = JSONRPCServer(server_url, request_timeout=5.0)
                
        try:
            # call some function on the server 
            result = yield server.foo(1, 2)
        except ProtocolError as err:
            logging.error('Some RPC error %s, %s', err.code, err)
        except TransportError as err:
            # err.args[1] refers to appropriate HTTPError
            logging.error('Transport error %s', err.args[1])


TODO
----

* Tests


Credits
-------

Based on `jsonrpc_requests <http://github.com/gciotta/jsonrpc-requests>` by `Giuseppe Ciotta <gciotta@gmail.com>`_.

