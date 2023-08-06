Python 3 Port of Pika, an AMQP 0-9-1 client library for Python
==============================================================

|Version| |Downloads| |Status| |Coverage| |License|

Introduction
-------------
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries
to stay fairly independent of the underlying network support library.

- Supports Python 3.2+ only.

- Since threads aren't appropriate to every situation, it doesn't
  require threads. It takes care not to forbid them, either. The same
  goes for greenlets, callbacks, continuations and generators. It is
  not necessarily thread-safe however, and your milage will vary.

- People may be using direct sockets, `asyncore`, plain old `select()`,
  or any of the wide variety of ways of getting network events to and from a
  python application. Pika tries to stay compatible with all of these, and to
  make adapting it to a new environment as simple as possible.

This is a Pika fork allowing you to tune the pika client properties. 
Waiting pull request (https://github.com/pika/pika/pull/571) to be merged or 
getting similar functionality on pika master before removing this fork.


Documentation
-------------

Pika's documentation is now at https://pika.readthedocs.org


Example
-------
Here is the most simple example of use, sending a message with the BlockingConnection adapter:

.. code :: python 

    import pika
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.basic_publish(exchange='example',
                          routing_key='test',
                          body='Test Message')
    connection.close()

And an example of writing a blocking consumer:

.. code :: python 

    import pika
    connection = pika.BlockingConnection()
    channel = connection.channel()

    for method_frame, properties, body in channel.consume('test'):

        # Display the message parts and ack the message
        print method_frame, properties, body
        channel.basic_ack(method_frame.delivery_tag)

        # Escape out of the loop after 10 messages
        if method_frame.delivery_tag == 10:
            break

    # Cancel the consumer and return any pending messages
    requeued_messages = channel.cancel()
    print 'Requeued %i messages' % requeued_messages
    connection.close()

And an example of tuning your client properties through Pika

.. code :: python

    import pika
    client_properties = {
        'product': 'my product',
        'information': 'my information',
        'my_other_props': 'my other property'
    }

    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters("localhost", 5672, '/',
                                           credentials=credentials, client_props=client_properties)
    connection = pika.BlockingConnection(parameters)

Pika provides the following adapters
------------------------------------

- AsyncoreConnection - based off the standard Python library asyncore
- BlockingConnection - enables blocking, synchronous operation on top of library for simple uses
- LibevConnection    - adapter for use with the libev event loop http://libev.schmorp.de
- SelectConnection   - fast asynchronous adapter
- TwistedConnection  - adapter for use with the Twisted asynchronous package http://twistedmatrix.com/
- TornadoConnection  - adapter for use with the Tornado IO Loop http://tornadoweb.org

License
-------
Pika is licensed under the MPLv2. If you have any questions regarding licensing,
please contact the RabbitMQ team at <info@rabbitmq.com>.


.. |Status| image:: https://travis-ci.org/renshawbay/pika-python3.svg?branch=python3
   :target: https://travis-ci.org/renshawbay/pika-python3

.. |License| image:: https://pypip.in/license/pika/badge.svg?
   :target: https://pika.readthedocs.org
