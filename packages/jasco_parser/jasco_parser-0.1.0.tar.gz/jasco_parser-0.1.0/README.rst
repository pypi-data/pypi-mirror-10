jasco_parser
==========================
.. image:: https://secure.travis-ci.org/lambdalisue/jasco_parser.png?branch=master
    :target: http://travis-ci.org/lambdalisue/jasco_parser
    :alt: Build status

.. image:: https://coveralls.io/repos/lambdalisue/jasco_parser/badge.png?branch=master
    :target: https://coveralls.io/r/lambdalisue/jasco_parser/
    :alt: Coverage

.. image:: https://pypip.in/py_versions/jasco_parser/badge.svg
    :target: https://pypi.python.org/pypi/jasco_parser/
    :alt: Supported Python versions
    
.. image:: https://pypip.in/status/jasco_parser/badge.svg
    :target: https://pypi.python.org/pypi/jasco_parser/
    :alt: Development Status
    
.. image:: https://pypip.in/d/jasco_parser/badge.svg
    :target: https://pypi.python.org/pypi/jasco_parser/
    :alt: Downloads

.. image:: https://pypip.in/v/jasco_parser/badge.svg
    :target: https://pypi.python.org/pypi/jasco_parser/
    :alt: Latest version

.. image:: https://pypip.in/wheel/jasco_parser/badge.svg
    :target: https://pypi.python.org/pypi/jasco_parser/
    :alt: Wheel Status

.. image:: https://pypip.in/egg/jasco_parser/badge.svg
    :target: https://pypi.python.org/pypi/jasco_parser/
    :alt: Egg Status

.. image:: https://pypip.in/license/jasco_parser/badge.svg
    :target: https://pypi.python.org/pypi/jasco_parser/
    :alt: License
    
.. image:: https://requires.io/github/lambdalisue/jasco_parser/requirements.svg?branch=master
    :target: https://requires.io/github/lambdalisue/jasco_parser/requirements/?branch=master
    :alt: Requirements Status
.. image:: https://landscape.io/github/lambdalisue/jasco_parser/master/landscape.png
    :target: https://landscape.io/github/lambdalisue/jasco_parser/master
    :alt: Code Health
   
Author
    Alisue <lambdalisue@hashnote.net>
Supported python versions
    Python 2.6, 2.7, 3.2, 3.3, 3.4

A text parser for parsing [JASCO](http://www.jasco.co.jp/jpn/home/index.html) style text.

Installation
------------
Use pip_ like::

    $ pip install jasco_parser

.. _pip:  https://pypi.python.org/pypi/pip

Usage
-----

.. code:: python

    from jasco_parser import load

    X = load('filename.txt')
