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
            self.regexp = options['strfmt']
        else:
            raise SyntaxError, "Must specify strfmt"
        if 'order' in options:
            self.order = options['order']

    def __iter__(self):
        for item in self.previous:

#            if self.key in item:
#                item[key] = self.apply_regex(

            yield item

    def slugify(self, _path):
        """
        If a _path like this is discovered:

            /path/to/content/2000/01/01/foo/index.html

        Change _path to:

            /path/to/content/foo-20000101.html
        """
#        expr = re.compile('(.*)(\d\d\d\d)/(\d\d)/(\d\d)/(.+)/index.html')
        expr = re.compile('(\d\d\d\d)/(\d\d)/(\d\d)/(.+)/index.html')
        result = expr.search(_path)
        if result:
            groups = result.groups()
#            _path = '%s/%s-%s%s%s.html' % (groups[0], groups[4], groups[1],
#                groups[2], groups[3])
            _path = '%s-%s%s%s.html' % (groups[3], groups[0],
                groups[1], groups[2])
        return _path

