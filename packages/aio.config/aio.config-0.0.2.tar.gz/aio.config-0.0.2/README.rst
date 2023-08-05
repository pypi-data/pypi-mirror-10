
aio.config
==========

Configuration utilities for the aio_ asyncio framework

.. _aio: https://github.com/phlax/aio


Build status
------------

.. image:: https://travis-ci.org/phlax/aio.config.svg?branch=master
	       :target: https://travis-ci.org/phlax/aio.config


Installation
------------

Install with:

.. code:: bash

	  pip install aio.config


Configuration finder
--------------------

The configuration finder will search the following directory paths in search of configuration files

- aio.conf

- etc/aio.conf

- /etc/aio.conf


Configuration parser
--------------------

The configuration parser uses *configparser.ExtendedInterpolation*
