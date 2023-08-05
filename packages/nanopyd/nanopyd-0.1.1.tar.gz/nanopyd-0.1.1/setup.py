# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nanopyd']

package_data = \
{'': ['*']}

install_requires = \
['pycryptodome>=3.12.0,<4.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'pytest>=6.2.5,<7.0.0']

setup_kwargs = {
    'name': 'nanopyd',
    'version': '0.1.1',
    'description': 'nanoid implementation in python',
    'long_description': '## NanoPyD\n\n### Python NanoID with class typing.\n\nBuilds a Nano ID per spect defined by [this repo](https://github.com/ai/nanoid).\n\n## Installation and Usage:\n\nTo install:\n`pip install nanopyd`\nImport:\n`from nanopyd import NanoID`\nUsage (with typing):\n`id : NanoID = NanoID()`\n\n### Parameters:\n\n1. alphabet :\n   - **"alphanumeric"**= "\\_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"\n   - "uppercase" = "\\_-ABCDEFGHIJKLMNOPQRSTUVWXYZ"\n   - "lowercase" = "\\_-abcdefghijklmnopqrstuvwxyz"\n   - "numbers" = "0123456789"\n   - "no_lookalikes" = "\\*-23456789abcdefghjkmnpqrstwxyzABCDEFGHJKMNPQRSTWXYZ"\n2. size :\n   - length of output id, default **21**\n',
    'author': 'yudjinn',
    'author_email': 'yudjinncoding@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yudjinn/nanopyd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
