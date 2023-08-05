Kantonzugpdf
============

A library to create PDF reports for the Canton of Zug

Usage
-----

Create a subclass of ReportZug and provide the populate method. To generate
the PDF, call build.

SVG
---
This package uses svglib which does not run properly with Python 3. To use
SVG files with Python 2, install the svglib package. To use this package with
Python 3, make sure get_logo of your report return None.


Run the Tests
-------------

Install tox and run it::

    pip install tox
    tox

Limit the tests to a specific python version::

    tox -e py27

Conventions
-----------

Kantonzugpdf follows PEP8 as close as possible. To test for it run::

    tox -e pep8

Kantonzugpdf uses `Semantic Versioning <http://semver.org/>`_

Build Status
------------

.. image:: https://travis-ci.org/seantis/kantonzugpdf.png
  :target: https://travis-ci.org/seantis/kantonzugpdf
  :alt: Build Status

Coverage
--------

.. image:: https://coveralls.io/repos/seantis/kantonzugpdf/badge.png?branch=master
  :target: https://coveralls.io/r/seantis/kantonzugpdf?branch=master
  :alt: Project Coverage

Latests PyPI Release
--------------------
.. image:: https://pypip.in/v/kantonzugpdf/badge.png
  :target: https://crate.io/packages/kantonzugpdf
  :alt: Latest PyPI Release

License
-------
kantonzugpdf is released under GPLv2
