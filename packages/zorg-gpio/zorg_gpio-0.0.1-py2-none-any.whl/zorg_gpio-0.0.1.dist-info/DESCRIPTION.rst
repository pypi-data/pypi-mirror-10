zorg-gpio
=========

|Build Status| |Code Climate| |Coverage Status|

Zorg (https://zorg-framework.github.io/) is a Python framework for
robotics and physical computing.

This module provides drivers for `General Purpose Input/Output
(GPIO) <https://en.wikipedia.org/wiki/General_Purpose_Input/Output>`__
devices. Typically, this library is registered by an adaptor class such
as ``zorg-edison`` (https://github.com/zorg/zorg-edison) that supports
the needed interfaces for GPIO devices.

Getting Started
---------------

Install the module with: ``pip install zorg zorg-gpio``

Example
-------

.. code:: python

    import time
    import zorg


    def blink_led(my):
        while True:
            my.led.toggle()
            time.sleep(100)

    robot = zorg.robot({
        "name": "Test",
        "connections": {
            "edison": {
                "adaptor": "zorg_edison.Edison",
            },
        },
        "devices": {
            "led": {
                "connection": "edison",
                "driver": "zorg_gpio.Led",
                "pin": 4, # Digital pin 4
            },
        },
        "work": blink_led,
    })

    robot.start()

Hardware Support
----------------

Zorg has a extensible system for connecting to hardware devices. The
following GPIO devices are currently supported:

-  Analog Sensor
-  Temperature sensor
-  Microphone
-  Light sensor
-  Touch sensor
-  Rotary Angle Sensor
-  Button
-  LED
-  Relay
-  Servo
-  Buzzer

`Open a new
issue <https://github.com/zorg-framework/zorg-gpio/issues/new>`__ to
request support for additional components.

License
-------

`Copyright (c) 2015 Team
Zorg <https://github.com/zorg-framework/zorg/blob/master/LICENSE.md>`__

.. |Build Status| image:: https://travis-ci.org/zorg-framework/zorg-gpio.svg
   :target: https://travis-ci.org/zorg-framework/zorg-gpio
.. |Code Climate| image:: https://codeclimate.com/github/zorg-framework/zorg-gpio/badges/gpa.svg
   :target: https://codeclimate.com/github/zorg-framework/zorg-gpio
.. |Coverage Status| image:: https://img.shields.io/coveralls/zorg-framework/zorg-gpio.svg
   :target: https://coveralls.io/r/zorg-framework/zorg-gpio


