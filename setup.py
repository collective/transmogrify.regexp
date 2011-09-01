
from setuptools import setup, find_packages

setup(
    entry_points={
        'z3c.autoinclude.plugin': 'target = transmogrify',
    }
    name='transmogrify.regexp',
    namespace_packages=['transmogrify'],
    packages=find_packages(),
    version='0.1.0',
)
