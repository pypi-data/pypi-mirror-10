sqlalchemy-nuodb
================

.. image:: https://img.shields.io/github/license/nuodb/sqlalchemy-nuodb.svg?style=flat
    :target: http://badges.mit-license.org
.. image:: https://img.shields.io/badge/python-2.7-blue.svg?style=flat
    :target: https://pypi.python.org/pypi/sqlalchemy-nuodb/
.. image:: https://travis-ci.org/nuodb/sqlalchemy-nuodb.svg?branch=master
    :target: https://travis-ci.org/nuodb/sqlalchemy-nuodb
.. image:: https://gemnasium.com/nuodb/sqlalchemy-nuodb.svg
    :target: https://gemnasium.com/nuodb/sqlalchemy-nuodb
.. image:: https://landscape.io/github/nuodb/sqlalchemy-nuodb/master/landscape.svg?style=flat
   :target: https://landscape.io/github/nuodb/sqlalchemy-nuodb/master
   :alt: Code Health

Introduction
------------

A SQLAlchemy driver for NuoDB.

Documentation
-------------

Latest documentation is at:

http://www.sqlalchemy.org/docs/

Version
-------

2.3.1 (June 30, 2015)

Requirements
------------

- Python 2.7.6
- SQLAlchemy 1.0.4

For those also interested in Flask and Sandman, here is the complete list of
dependencies and their version numbers; this stack has been tested together:

- PyNuoDB 2.3.1, or later
- SQLAlchemy 1.0.1, or later (preferentially 1.0.4)
- Flask 0.10.1
- Flask-Alchemy 1.0
- Sandman 0.2

Installation
------------

Standard Python setup should be used:

    | python setup.py install

Full documentation for installation of SQLAlchemy is at
`Installation <http://www.sqlalchemy.org/docs/intro.html#installation>`_.

License
-------

SQLAlchemy/NuoDB is distributed under the `MIT license
<http://www.opensource.org/licenses/mit-license.php>`_.

Connections
-----------

A TCP/IP connection can be specified as the following:

    | from sqlalchemy import create_engine
    |
    | e = create_engine("nuodb://user:pass@host[:port]/database[?schema=schema-name]")
