==================================
Welcome to aiomas's documentation!
==================================

`PyPI <https://pypi.python.org/pypi/aiomas>`_ |
`Bitbucket <https://bitbucket.org/ssc/aiomas>`_ |
`Mailing list <https://groups.google.com/forum/#!forum/aiomas>`_ |
IRC: #aiomas

*aiomas* is an easy-to-use library for *remote procedure calls (RPC)* and
*multi-agent systems (MAS)*. It’s written in pure Python on top of asyncio__.

Here is an example how you can write a simple multi-agent system:

.. code-block:: python

   >>> import asyncio
   >>> import aiomas
   >>>
   >>> class TestAgent(aiomas.Agent):
   ...     def __init__(self, container, addr):
   ...         super().__init__(container, addr)
   ...         print('Ohai, I am %s' % self)
   ...
   ...     @asyncio.coroutine
   ...     def run(self, addr):
   ...         remote_agent = yield from self.container.connect(addr)
   ...         ret = yield from remote_agent.service(42)
   ...         print('%s got %s from %s' % (self, ret, remote_agent))
   ...
   ...     @aiomas.expose
   ...     def service(self, value):
   ...         return value
   >>>
   >>> c = aiomas.Container(('localhost', 5555))
   >>> agents = [c.spawn(TestAgent) for i in range(2)]
   Ohai, I am TestAgent('tcp://localhost:5555/0')
   Ohai, I am TestAgent('tcp://localhost:5555/1')
   >>> aiomas.run(until=agents[0].run(agents[1].addr))
   TestAgent('tcp://localhost:5555/0') got 42 from TestAgentProxy('tcp://localhost:5555/1')
   >>> c.shutdown()

*aiomas* is released under the MIT license. It requires Python 3.4 and above
and runs on Linux, OS X, and Windows.

__ https://docs.python.org/3/library/asyncio.html


Contents:
=========

.. toctree::
   :maxdepth: 2

   overview
   agent
   rpc
   channel
   codecs
   clocks
   testing
   api_reference/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
