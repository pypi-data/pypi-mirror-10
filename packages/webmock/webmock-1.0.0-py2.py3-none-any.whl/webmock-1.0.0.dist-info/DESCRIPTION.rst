webmock
=======

This tool provides an in-process WSGI server on an ephemeral port.
It is intended for use in unit tests, when the system under test makes outgoing HTTP connections that cannot easily be mocked.

Usage
-----

First, create a WSGI application that represents the fake web server you want to create.
This is simpler than it seems; for example::

    def simple_app(environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return ['Hello, world!\n']

Next, activate the test server.
There are several ways to do this, but all of them produce a port number.

As a context manager::

    from mockweb import mock_server
    def test_web_request():
        with mock_server(simple_app) as port:
            my_client.get_greeting('http://127.0.0.1:{}'.format(port))

As a decorator::

    from mockweb import mock_server
    @mock_server(simple_app)
    def test_web_request(port):
        my_client.get_greeting('http://127.0.0.1:{}'.format(port))

Or manually started and stopped::

    from mockweb import mock_server
    @mock_server
    def test_web_request():
        server = mock_server(simple_app)
        # ...
        server.start()
        my_client.get_greeting('http://127.0.0.1:{}'.format(port))
        server.stop()

In the latter case, be careful to stop the server.


