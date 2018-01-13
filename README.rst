
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ft62xx/badge/?version=latest

    :target: https://circuitpython.readthedocs.io/projects/ft62xx/en/latest/

    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

CircuitPython driver for common low-cost FocalTech capacitive touch chips.
Currently supports FT6206

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block:: python

	import time
	import busio
	import board
	from ft62xx import adafruit_ft62xx

	# Create library object using our Bus I2C port
	i2c = busio.I2C(board.SCL, board.SDA)

	ft = adafruit_ft62xx.Adafruit_FT6206(i2c, debug=True)

	while True:
	    n = ft.touched
	    if n:
        	print(ft.touches)

API Reference
=============

.. toctree::
   :maxdepth: 2

   api

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_ft62xx/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-ft62xx --library_location .
