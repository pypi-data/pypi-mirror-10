=====================
gpsdio density plugin
=====================


.. image:: https://travis-ci.org/SkyTruth/gpsdio-density.svg?branch=master
    :target: https://travis-ci.org/SkyTruth/gpsdio-density


.. image:: https://coveralls.io/repos/SkyTruth/gpsdio-density/badge.svg?branch=master
    :target: https://coveralls.io/r/SkyTruth/gpsdio-density


A CLI plugin for `gpsdio <https://github.com/skytruth/gpdsio/>`_ that creates density rasters.


Examples
--------

See ``gpsdio density --help`` for info.

.. code-block:: console

    $ gpsdio density tests/data/*.json example-density.tif \
        -c COMPRESS=DEFLATE \
        -c TILED=YES \
        -c PREDICTOR=2 \
        --jobs 2


Installing
----------

Via pip:

.. code-block:: console

    $ pip install gpsdio-density

From master:

.. code-block:: console

    $ git clone https://github.com/SkyTruth/gpsdio-density
    $ cd gpsdio-density
    $ pip install .


Developing
----------

.. code-block::

    $ git clone https://github.com/SkyTruth/gpsdio-density
    $ cd gpsdio-density
    $ virtualenv venv && source venv/bin/activate
    $ pip install -e .[test]
    $ py.test tests --cov gpsdio_density --cov-report term-missing
