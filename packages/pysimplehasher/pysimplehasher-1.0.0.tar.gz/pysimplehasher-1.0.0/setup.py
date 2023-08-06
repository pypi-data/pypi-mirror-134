# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pysimplehasher']
setup_kwargs = {
    'name': 'pysimplehasher',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'Xenely',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
