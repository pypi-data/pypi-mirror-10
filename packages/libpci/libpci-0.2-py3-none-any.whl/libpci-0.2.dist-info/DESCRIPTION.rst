==========================================
Pure Python, high-level bindings to libpci
==========================================

.. image:: https://badge.fury.io/py/libpci.png
    :target: http://badge.fury.io/py/libpci

.. image:: https://travis-ci.org/zyga/libpci.png?branch=master
        :target: https://travis-ci.org/zyga/libpci

.. image:: https://pypip.in/d/libpci/badge.png
        :target: https://pypi.python.org/pypi/libpci

Features
========

* Free software: LGPLv3 license
* Documentation: https://libpci.readthedocs.org.
* Use high-level, pythonic APIs to work with libpci





History
=======

0.2 (2015-04-24)
----------------

* Use sub-commands for easier extensibility and less ambiguity.
* Move all flag control options to the 'pci-lookup' command.
* Move the PCI device and vendor name look up to their own sub-commands.
* Add LibPCI.lookup_subsystem_device_name().
* Add 'subsystem-device' sub-command.

0.1.1 (2015-04-23)
------------------

* Fix architecture detection bug that prevented libpci from working on Fedora.

0.1 (2015-04-23)
----------------

* First release on PyPI.


