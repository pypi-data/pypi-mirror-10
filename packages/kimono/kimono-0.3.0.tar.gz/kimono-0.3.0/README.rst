kimono
======

USAGE


.. code:: python

    from kimono import Kimono
    api = Kimono('APIKEY', 'APIID')

IMPLEMENTED

Fetch data from an API

.. code:: python

    # Normal
    api.api_data()

    # On Demand
    api = Kimono('APIKEY', 'APIID', ondemand=True)
    api.api_data()

`Retrieve an API <https://www.kimonolabs.com/apidocs#RetrieveApi>`__

.. code:: python

    api.retrieve_api()

`List all APIs <https://www.kimonolabs.com/apidocs#ListApis>`__

.. code:: python

    api.list_apis()
