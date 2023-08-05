Neokami Python SDK v0.1
=======================

This SDK allows you to connect your Python web-applications to the
Neokami SDK.

In order to use the SDK, you need to obtain a free API Key from
`www.neokami.com`_.

Installation
============

-  via pip:

   ::

       pip install neokami-sdk

   Inside your python project

   .. code:: python

       import neokami

Usage
=====

Here is a simple usage example for gender & age detection for images:

.. code:: python

    import neokami
    import os

    req = neokami.ImageAnalyser()
    directory = os.path.dirname(os.path.abspath(__file__))
    req.setFile(directory + '/data/team1.jpg')
    req.setApiKey('your api key here')
    req.setWait(1)
    analysis = req.analyse()

    #get the results
    results = analysis.result()

Chained function calls are also supported for syntax brevity:

.. code:: python

    import os
    import neokami

    directory = os.path.dirname(os.path.abspath(__file__))
    analysis = neokami.ImageAnalyser().setApiKey(NeokamiTestCredentials.api_key).setFile(directory +'/data/team1.jpg').analyse()

**For a full documentation, check out the wiki:**

`Neokami Wiki`_

Tests
-----

-  To run the tests, the pytest package is required:

   `Install pytest`_

   .. code:: bash

       pip install -U pytest # or
       easy_install -U pytest

-  Create a NeokamiTestCredentials.python inside the tests/ folder based
   on the template in NeokamiTestCredentials.python.replace and enter
   your API Key.

   Repository contributors can apply for api keys to be used inside unit
   tests at team@neokami.com.

-  The tests can be executed by running:

   .. code:: bash

       py.test

Contributing
------------

Coming soon.

.. _www.neokami.com: http://neokami.com/free-api-key/
.. _Neokami Wiki: http://docs.neokami.com/
.. _Install pytest: https://pytest.org/latest/getting-started.html