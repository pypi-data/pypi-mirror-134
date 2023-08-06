# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sign_off']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['sign-off = sign_off.sign_off:main']}

setup_kwargs = {
    'name': 'sign-off',
    'version': '0.0.9',
    'description': 'pre-commit hook to add "signed-off-by" line to commit messages',
    'long_description': None,
    'author': 'dynobo',
    'author_email': 'dynobo@mailbox.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
