========
str2type
========

Convert the string representation of a Python type to its native type.

.. image:: https://travis-ci.org/geowurster/str2type.svg?branch=master
    :target: https://travis-ci.org/geowurster/str2type?branch=master

.. image:: https://coveralls.io/repos/geowurster/str2type/badge.svg?branch=master
    :target: https://coveralls.io/r/geowurster/str2type?branch=master


Why?
====

When building commandline utilities the syntax ``--arg key=val`` is useful,
especially when ``key`` and ``val`` will be used as ``Class(key=val)`` internally.
This module was built specifically to be used with the CLI framework `click <http://click.pocoo.org/>`_, and the
included extensions play nicely, but the ``str2type.str2type()`` function can be
used elsewhere.


Examples
========

See the ``examples`` directory for `click integration examples <https://github.com/mitsuhiko/click>`_.  Everything else is primarily handled
by a single function:

.. code-block:: python

    >>> from str2type import str2type
    >>> print(str2type("1.23"))
    1.23
    >>> print(str2type("1.")
    1.0
    >>> print(str2type(".2"))
    0.2
    >>> print(str2type("None"))
    None
    >>> print(str2type('String'))
    'String'


Supported Types
===============

Only the standard builtin Python types plus JSON strings are supported:

- ``int``
- ``float``
- ``None``
- ``True``
- ``False``
- ``JSON``



Installing
==========

Via pip:

.. code-block:: console

    $ pip install str2type

From master branch:

.. code-block:: console

    $ git clone https://github.com/geowurster/str2type
    $ cd str2type
    $ pip install .


Developing
==========

Install:

.. code-block:: console

    $ pip install virtualenv
    $ git clone https://github.com/geowurster/str2type
    $ cd str2type
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements-dev.txt -e .
    $ nosetests --with-coverage
    $ pep8 --max-line-length=95 str2type
