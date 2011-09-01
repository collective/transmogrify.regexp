
from setuptools import setup, find_packages

setup(
    name='transmogrify.regexp',
    namespace_packages=['transmogrify'],
    packages=find_packages(),
    entry_points={
        'z3c.autoinclude.plugin': 'target = transmogrify',
    }
)
