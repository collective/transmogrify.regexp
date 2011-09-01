Introduction
============

``transmogrify.regexp`` allows you to use regular expressions and format strings
to search and replace key values in a transmogrifier pipeline.

Installation
============

Usage
=====

Sample usage::

    [apply_regexp]
    blueprint = transmogrify.regexp
    key = _path
    expression = /(.*)/(\d\d\d\d)/(\d\d)/(\d\d)/(.+)/index.html
    format = %%s/%%s-%%s%%s%%s.html
    order = 0,4,1,2,3
