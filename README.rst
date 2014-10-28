Introduction
============

``transmogrify.regexp`` allows you to use regular expressions and format strings
to search and replace key values in a transmogrifier pipeline.

Features
--------

- Using regular expressions with ``re`` python module.

- *Search* and *replace* with format strings.

- Sorting based in *groups* regular expressions defined.

Installation
============

Make sure to require ``transmogrify.regexp`` as an ``install_requires`` in the
``setup.py`` file in your project, e.g.::

        install_requires=[
            ...
            'transmogrify.regexp',
        ]


Usage
=====

This packahe provided a blueprint.


transmogrify.regexp
-------------------

This blueprint let you modify key values by applying a regular expression.

The options are:

:key:
  Defines which key must be apply the regular expression defined in the
  ``expression`` option.

:expression:
  Defines the criteria regular expression to search.

:format:
  Defines the string format which to apply the replacement.

:order:
  Defines the desired order of the groups ``()`` regular expressions defined
  in the ``expression`` option, ie, the original order of the groups in the
  expression starts in 0 as a succession then you can changing of sorting to
  match the format of the string of ``format`` option.


Example
-------

Then a sample usage in your pipelines: ::

  [apply_regexp]
  blueprint = transmogrify.regexp
  key = _path
  expression = /(.*)/(\d\d\d\d)/(\d\d)/(\d\d)/(.+)/index.html
  format = %%s/%%s-%%s%%s%%s.html
  order = 0,4,1,2,3

This example requires changing the order of a string, whose initial
value is ``/blog/2014/09/22/plone/index.html`` by this new value
``/blog/plone-20140922.html``.

The options are explains are following:

* The ``key`` option defines the ``_path`` key which must be applied
  the regular expression defined in the ``expression`` option.

* The ``expression`` option defined the criteria to search like this
  ``/(.*)/(\d\d\d\d)/(\d\d)/(\d\d)/(.+)/index.html``.

* The ``format`` option defines the string format which must be applied
  the replacement like this ``%%s/%%s-%%s%%s%%s.html``.

* The ``order`` option defines the desired order of the groups ``()``
  regular expressions defined like this ``0,4,1,2,3`` to match the
  string format of ``format`` option.

See also
--------

* `Regular expression operations with Python 2.7.8 <https://docs.python.org/2/library/re.html>`_.

* `RegExr: Learn, Build, & Test RegEx <http://www.regexr.com/>`_.

Contribute
==========

* Issue Tracker: http://github.com/collective/transmogrify.regexp/issues

* Source Code: http://github.com/collective/transmogrify.regexp

* Documentation: https://github.com/collective/transmogrify.regexp/blob/master/README.rst
