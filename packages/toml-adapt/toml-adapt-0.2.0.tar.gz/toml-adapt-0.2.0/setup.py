# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['toml_adapt']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0', 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['toml-adapt = toml_adapt.main:TomlAdapt']}

setup_kwargs = {
    'name': 'toml-adapt',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'iztokf',
    'author_email': 'iztokf@fedoraproject.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
