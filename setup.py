
from setuptools import setup, find_packages

setup(
    description='Modify key values by applying a regular expression',
    entry_points={
        'z3c.autoinclude.plugin': 'target = transmogrify',
    },
    long_description=open('README.rst').read(),
    name='transmogrify.regexp',
    namespace_packages=['transmogrify'],
    packages=find_packages(),
    url='https://github.com/aclark4life/transmogrify.regexp',
    version='0.3.0',
)
