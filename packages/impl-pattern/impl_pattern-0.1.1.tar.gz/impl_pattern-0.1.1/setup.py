# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['impl_pattern']

package_data = \
{'': ['*']}

install_requires = \
['asyncio>=3.4,<4.0']

setup_kwargs = {
    'name': 'impl-pattern',
    'version': '0.1.1',
    'description': '',
    'long_description': '## Implements the `impl` pattern*\n\n/* *inspired by Rust*\n\nUseful when it is needed to extend a class (usually 3d party) with some methods\n\n### Install\n\n```shell\npip install impl_pattern\n```\n\nor\n\n```shell\npoetry add impl_pattern\n```\n\n### Usage\n\n#### Regular methods\n\n```python\nfrom impl_pattern import impl\n\nclass Sample:\n    def __init__(self):\n        self.value = 10\n\n@impl(Sample)\ndef plus_one(self: Sample):\n    self.value += 1\n\ns = Sample()\ns.plus_one()\n\nprint(s.value) \n# 11\n```\n\nit works with async methods as well\n\n```python\nfrom asyncio import sleep\n\n@impl(Sample)\nasync def plus_one(self: Sample):\n    await sleep(1)\n    self.value += 1\n\ns = Sample()\nawait s.plus_one()\n\nprint(s.value) \n# 11\n```\n\n#### Class methods\n\nTo register function as a classmethod you can use `impl_classmethod` decorator\n\n```python\nfrom impl_pattern import impl_classmethod\n\nclass Sample:\n    value = 10\n\n@impl_classmethod(Sample)\ndef plus_one(cls):\n    cls.value += 1\n\nSample.plus_one()\n\nprint(Sample.value) \n# 11\n```\n\nThis works with async methods too\n\n```python\nfrom asyncio import sleep\n\n@impl_classmethod(Sample)\nasync def plus_one(cls):\n    await sleep(1)\n    self.value += 1\n\nawait Sample.plus_one()\n\nprint(Sample.value) \n# 11\n```\n\n#### Static methods\n\nStatic methods use the same syntax but with the `impl_staticmethod` decorator\n\n```python\nfrom impl_pattern import impl_staticmethod\n\nclass Sample:\n    ...\n\n@impl_staticmethod(Sample)\ndef get_one():\n    return 1\n\nprint(Sample.get_one()) \n# 1\n```\n\nThis works with async methods too\n\n```python\nfrom asyncio import sleep\n\n@impl_staticmethod(Sample)\nasync def get_one():\n    return 1\n\nprint(await Sample.get_one()) \n# 1\n```',
    'author': 'Roman',
    'author_email': 'roman-right@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/roman-right/impl_pattern',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
