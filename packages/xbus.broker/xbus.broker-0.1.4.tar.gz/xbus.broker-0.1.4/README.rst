xbus.broker
===========

xbus.broker is the central piece of the Xbus project.

Related projects:
  - xbus.file_emitter <https://bitbucket.org/xcg/xbus.file_emitter>
  - xbus.monitor <https://bitbucket.org/xcg/xbus.monitor>
  - xbus_monitor_js <https://bitbucket.org/xcg/xbus_monitor_js>


Xbus
----

Xbus is an Enterprise service bus. As such it aims to help IT departments
achieve a better application infrastructure layout by providing a way to
urbanize the IT systems.

The goals of urbanization are:
  - high coherence
  - low coupling

More information about Xbus:
  - Documentation: <http://xbusbroker.readthedocs.org/>
  - Website: <https://xbus.io/>
  - Presentation in French: <http://bit.ly/1AYtQa6>


Installing
----------

Get requirements: 0mq, python3 and redis::

  $ sudo apt-get install libzmq3-dev python3 redis-server

Set up a virtualenv::

  $ mkvirtualenv xbus

Install the xbus.broker package::

  $ pip install xbus.broker


Configuring
-----------

Create configuration files (eg for the 0.1.3 version)::

  $ wget https://bitbucket.org/xcg/xbus.broker/raw/0.1.3/etc/config.ini-example -O config.ini
  $ wget https://bitbucket.org/xcg/xbus.broker/raw/0.1.3/etc/logging.ini-example -O logging.ini

Edit the files following comments written inside.
Note: Ensure the path to the logging file is an absolute path.


Initialize the database
-----------------------

Run the "setup_xbusbroker" program::

  $ setup_xbusbroker -c config.ini


Running
-------

Run the "start_xbusbroker" program::

  $ start_xbusbroker -c config.ini
