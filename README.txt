Introduction
============

`transmogrify.regex` allows you to use regular expressions and format strings
to search and replace key values in a transmogrifier pipeline.

E.g.:

    [slugify]
    blueprint = transmogrify.regex
    key = _path
    regexp = (\d\d\d\d)/(\d\d)/(\d\d)/(.+)/index.html
    format = %s-%s%s%s.html
    order = (3, 0, 1, 2)
