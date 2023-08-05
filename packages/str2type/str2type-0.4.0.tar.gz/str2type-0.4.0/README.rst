========
str2type
========

Convert the string representation of a Python type to its native type.

.. image:: https://travis-ci.org/geowurster/str2type.svg?branch=master
    :target: https://travis-ci.org/geowurster/str2type?branch=master

.. image:: https://coveralls.io/repos/geowurster/str2type/badge.svg?branch=master
    :target: https://coveralls.io/r/geowurster/str2type?branch=master

Convert a string representation of an ``int``, ``float``, ``None``, ``True``, ``False`, or JSON
to its native type.  For None, True, and False, case is irrelevant.  The
primary use-case of this function is automatically parsing user-input from
the commandline into Python types.  Argument parsers usually handle this no
problem but if a flag can take multiple types then ``str2type()`` can serve
as the decoder.

    >>> from str2type import str2type
    >>> print(str2type("1.23"))
    1.23
    >>> print(str2type("1.")
    1.0
    >>> print(str2type(".2"))
    0.2
    >>> print(str2type("NonE"))
    None
    >>> print(str2type("String"))
    "String"


Installing
----------

Via pip:

    $ pip install str2type

From master branch:

    $ git clone https://github.com/geowurster/str2type
    $ cd str2type
    $ pip install .


Developing
----------

Install:

    $ pip install virtualenv
    $ git clone https://github.com/geowurster/str2type
    $ cd str2type
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements-dev.txt -e .
    $ nosetests --with-coverage
    $ pep8 --max-line-length=95 str2type
