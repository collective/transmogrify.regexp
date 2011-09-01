import re

from collective.transmogrifier.interfaces import ISectionBlueprint, ISection
from zope.interface import classProvides, implements


class ApplyRegex(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        if 'key' in options:
            self.key = options['key']
        else:
            raise SyntaxError, "Must specify key"
        if 'regexp' in options:
            self.regexp = options['regexp']
        else:
            raise SyntaxError, "Must specify regexp"
        if 'strfmt' in options:
            self.strfmt = options['strfmt'].replace('%%', '%')  # XXX Better way to unescape?
        else:
            raise SyntaxError, "Must specify strfmt"
        if 'order' in options:
            self.order = options['order']
        else:
            self.order = None

    def __iter__(self):
        for item in self.previous:
            if self.key in item:
                item[self.key] = self.apply_regex(item[self.key])
            yield item

    def apply_regex(self, _path):
        expr = re.compile(self.regexp)
        result = expr.search(_path)
        if result:
            groups = result.groups()
            if groups is not None:
                if self.order is not None:
                    _path = self.strfmt % tuple([groups[int(i)] for i in self.order.split(',')])
                else:
                    raise SyntaxError, "Must specify order"

        return _path
