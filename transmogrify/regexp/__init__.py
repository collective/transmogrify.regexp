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
        if 'expression' in options:
            self.regexp = options['expression']
        else:
            raise SyntaxError, "Must specify regexp"
        if 'format' in options:
            self.strfmt = options['format'].replace('%%', '%')  # XXX Better way to unescape?
        else:
            raise SyntaxError, "Must specify strfmt"
        if 'order' in options:
            self.order = options['order']
        else:
            self.order = None

    def __iter__(self):
        for item in self.previous:
            if self.key in item:
                item = self.apply_regex(item, self.key)
            
            yield item

    def apply_regex(self, item, key):
        expr = re.compile(self.regexp)
        result = expr.search(item[key])
        if result:
            groups = result.groups()
            if groups is not None:
                if self.order is not None:
                    item['_path'] = self.strfmt % tuple([groups[int(i)] for i in self.order.split(',')])
                    item['_regexp_applied'] = True
                else:
                    raise SyntaxError, "Must specify order"

        return item
