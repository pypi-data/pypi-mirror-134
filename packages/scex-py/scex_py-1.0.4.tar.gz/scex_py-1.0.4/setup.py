# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scex_py']

package_data = \
{'': ['*'], 'scex_py': ['input_xml/*', 'input_xml/balloon_payment/*']}

install_requires = \
['requests>=2.26.0,<2.27.0', 'xmltodict>=0.12.0,<0.13.0']

setup_kwargs = {
    'name': 'scex-py',
    'version': '1.0.4',
    'description': '',
    'long_description': None,
    'author': 'Jatin Goel',
    'author_email': 'jatin.goel@thesummitgrp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
