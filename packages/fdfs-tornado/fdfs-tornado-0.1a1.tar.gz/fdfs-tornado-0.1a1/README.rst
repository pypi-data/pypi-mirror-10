===============================
Async FDFS Client for tornado
===============================

This library provides an async FDFS client for tornado.

QuickStart
===========

install using pip::

    $ pip install fdfs-tornado


Basic Usage
============

init a client
--------------

use ``tracker_ip`` and ``tracker_port`` to initialize the FDFS Client.
Create a single client for a specific case.

.. code-block:: python

    from fdfs_tornado.client import makeclient

    AsyncFDFSClient = makeclient(tracker_ip, tracker_port)
    client = AsyncFDFSClient()

.. note::

    the client will not create any connection before upload or download
    actions.

upload a file
--------------

To upload a file. First open the file in binary mode, and get the size, those
are required.

.. code-block:: python

    from tornado.ioloop import IOLoop
    ioloop = IOLoop.instance()

    client = AsyncFDFSClient()
    with open(filename, 'rb') as f:
        file_size = os.stat(filename).st_size
        future = client.upload(f, file_size)
        future.add_done_callback(lambda _: ioloop.close())
        ioloop.start()

        ret = future.result()
