=========================================================
pytwitcherapi
=========================================================

.. image:: http://img.shields.io/pypi/v/pytwitcherapi.png?style=flat
    :target: https://pypi.python.org/pypi/pytwitcherapi
    :alt: PyPI version

.. image:: https://pypip.in/py_versions/pytwitcherapi/badge.png?style=flat
    :target: https://pypi.python.org/pypi/pytwitcherapi/
    :alt: Supported Python versions

.. image::  https://img.shields.io/travis/Pytwitcher/pytwitcherapi/master.png?style=flat
    :target: https://travis-ci.org/Pytwitcher/pytwitcherapi
    :alt: Build Status

.. image:: https://pypip.in/status/pytwitcherapi/badge.png?style=flat
    :target: https://pypi.python.org/pypi/pytwitcherapi/
    :alt: Development Status

.. image:: https://pypip.in/format/pytwitcherapi/badge.png?style=flat
    :target: https://pypi.python.org/pypi/pytwitcherapi/
    :alt: Download format

.. image:: http://img.shields.io/pypi/dm/pytwitcherapi.png?style=flat
    :target: https://pypi.python.org/pypi/pytwitcherapi
    :alt: Downloads per month

.. image:: https://img.shields.io/coveralls/Pytwitcher/pytwitcherapi/master.png?style=flat
    :target: https://coveralls.io/r/Pytwitcher/pytwitcherapi
    :alt: Coverage

.. image:: http://img.shields.io/pypi/l/pytwitcherapi.png?style=flat
    :target: https://pypi.python.org/pypi/pytwitcherapi
    :alt: License

.. image:: https://readthedocs.org/projects/pytwitcherapi/badge/?version=latest&style=flat
    :target: http://pytwitcherapi.readthedocs.org/en/latest/
    :alt: Documentation



Twitch is a trademark or registered trademark of Twitch Interactive, Inc. in the U.S. and/or other countries. "pytwitcher" and "pytwitcherapi" is not operated by, sponsored by, or affiliated with Twitch Interactive, Inc. in any way.

Python API for interacting with `twitch.tv  <https://github.com/justintv/Twitch-API>`_.


Features
--------

* Easy-to-use object oriented high-level API
* Search and query information about games, channels, streams and users
* Get the livestream playlist
* OAauth Authentication. Can retrieve followed streams and more...
* Good documentation and test coverage


.. :changelog:

History
-------

0.1.1 (2015-03-15)
+++++++++++++++++++++++++++++++++++++++

* First release on PyPI.
* Pulled pytwitcherapi out of main project pytwitcher

0.1.2 (2015-03-15)
+++++++++++++++++++++++++++++++++++++++

* Fix wrapping search stream results due to incomplete channel json

0.1.3 (2015-03-23)
+++++++++++++++++++++++++++++++++++++++

* Refactor twitch module into models and session module

0.1.4 (2015-03-23)
+++++++++++++++++++++++++++++++++++++++

* Fix wrap json using actual class instead of cls

0.2.0 (2015-04-12)
+++++++++++++++++++++++++++++++++++++++

* Authentication: User can login and TwitchSession can retrieve followed streams.

0.3.0 (2015-05-08)
+++++++++++++++++++++++++++++++++++++++

* Easier imports. Only import the package for most of the cases.
* Added logging. Configure your logger and pytwitcher will show debug messages.

0.3.1 (2015-05-09)
+++++++++++++++++++++++++++++++++++++++

* Fix login server shutdown by correctly closing the socket


