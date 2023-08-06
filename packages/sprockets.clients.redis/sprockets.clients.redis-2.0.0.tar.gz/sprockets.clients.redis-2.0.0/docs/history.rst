.. :changelog:

Release History
===============

Next Release
------------

`2.0.0`_ (2015-06-22)
---------------------

* Backwards incompatible change to the ``RedisConnection`` class.  Inherit from ``StrictRedis`` instead of wrapping it.

`1.2.0`_ (2015-05-18)
---------------------

* Add a RedisConnection that is not sharded.

`1.1.0`_ (2015-05-18)
---------------------

* Add support for some set based functionality the redis client provides

`1.0.1`_ (2015-04-30)
---------------------

* Don't log the payload in the DEBUG level logs, causes an encoding error when it's not ascii


`1.0.0`_ (2015-03-30)
---------------------

* Initial release of the sharded redis connection.


.. _`1.1.0`: https://github.com/sprockets/sprockets.clients.redis/compare/1.0.1...1.1.0
.. _`1.0.1`: https://github.com/sprockets/sprockets.clients.redis/compare/1.0.0...1.0.1
.. _`1.0.0`: https://github.com/sprockets/sprockets.clients.redis/compare/0.0.0...1.0.0
