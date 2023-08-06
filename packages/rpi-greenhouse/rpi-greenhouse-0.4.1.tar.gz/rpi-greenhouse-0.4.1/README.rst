================================
Raspberry Pi Plantpot Greenhouse
================================

Python module for `Raspberry Pi`_ plantpot greenhouse add-on board produced by `Rachel Rayns`_. The library provides a simple interface to logging data from the board's sensors, controlling the board's LEDs and using them to display information from the sensors.

Components
==========

Sensors
-------

* Temperature and Humidity sensor (DHT22)
* Soil Moisture sesnsor
* Light sensor (LDR)

LEDs
----

* 3x white
* 3x red
* 3x blue
* 3x green
    
RTC
---

* Real Time Clock (DS1307)

Installation
============

Install the dependencies and install *rpi-greenhouse* with *pip*.

See full `installation instructions`_.

Python 3 is not currently supported due to a Python 2 -only dependency. This will be resolved as a priority to add Python 3 support.

Documentation
=============

Comprehensive documentation available at `pythonhosted.org/rpi-greenhouse`_

Contributors
============

* `Ben Nuttall`_
* `Tom Hartley`_
* `Luke Wren`_

Open Source
===========

* The code is licensed under the `BSD Licence`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues


.. _Raspberry Pi: https://www.raspberrypi.org/
.. _Rachel Rayns: https://github.com/RZRZR
.. _installation instructions: https://pythonhosted.org/rpi-greenhouse/installing/
.. _pythonhosted.org/rpi-greenhouse: https://pythonhosted.org/rpi-greenhouse/
.. _Ben Nuttall: https://github.com/bennuttall
.. _Tom Hartley: https://github.com/tomhartley
.. _Luke Wren: https://github.com/wren6991
.. _BSD Licence: http://opensource.org/licenses/BSD-3-Clause
.. _GitHub: https://github.com/bennuttall/rpi-greenhouse
.. _GitHub Issues: https://github.com/bennuttall/rpi-greenhouse/issues
