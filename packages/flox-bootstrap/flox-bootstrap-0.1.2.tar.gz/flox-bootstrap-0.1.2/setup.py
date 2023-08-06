# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flox_bootstrap']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'flox-core>=0.2,<1.0.0',
 'jinja2>=2.11,<3.0',
 'stringcase>=1.2,<2.0']

entry_points = \
{'flox.plugin': ['bootstrap = flox_bootstrap:plugin']}

setup_kwargs = {
    'name': 'flox-bootstrap',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Michal Przytulski',
    'author_email': 'michal@przytulski.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
