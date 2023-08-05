xbus.monitor
============

This package provides tools to monitor and administer Xbus <http://xbus.io>.

Note: this package provides a REST API but no GUI; separate packages implement
it.

Current packages providing an interface to xbus.monitor:

- xbus_monitor_js <https://bitbucket.org/xcg/xbus_monitor_js>: Single-page
  JavaScript Backbone application that communicates with xbus.monitor via its
  REST API.


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
  - Website: <http://xbus.io/>
  - Presentation: <http://bit.ly/1AYtQa6>


Installing
----------

Set up a virtualenv::

    $ mkvirtualenv xbus

Clone this project::

    $ hg clone ssh://hg@bitbucket.org/xcg/xbus.monitor

Install Python requirements::

  $ pip install -r xbus.monitor/requirements.txt

Then install the xbus.monitor package::

    $ pip install xbus.monitor


Configuring
-----------

Follow the xbus.broker README file to set it up.

Xbus monitor settings are within the etc/production-example.ini file::

    $ cp xbus.monitor/etc/production-example.ini monitor.ini

Edit the file following comments written inside.

Localization:

    Edit the "pyramid.default_locale_name" variable. Note: Only "en_US" and
    "fr_FR" are supported for now.


Running
-------

Run as a regular Pyramid program::

  $ pserve monitor.ini


Run tests
---------
::

    nosetests


Generate the translation template
---------------------------------
::

    pip install Babel lingua
    python setup.py extract_messages


Other translation tasks
-----------------------
See <http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/i18n.html>.
::

    python setup.py [init_catalog -l en_US] [update_catalog] [compile_catalog]


Thanks
------

xbus.monitor uses the following external projects; thanks a lot to their respective authors:
    - pyramid <http://docs.pylonsproject.org/projects/pyramid/en/latest/>
    - pyramid_httpauth <https://github.com/tarzanjw/pyramid_httpauth>
