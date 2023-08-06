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
    'version': '0.1.3',
    'description': 'Bootstrap your project with predefined templates',
    'long_description': '# flox bootstrap engine\n\nCreate your projects in seconds with [flox](https://github.com/getflox/flox) using shared templates. \n\n## Installation\n\n```bash\n$ flox plugin install flox-bootstrap\n```\n\nor\n\n```bash\n$ pip install flox-bootstrap\n```\n\n## Configuration\n\nYou can use this plugin without any configuration, but if you like you can add your own custom repository \nwhich may contain additional or customised templates. \n\n```bash\n$ flox config --plugin bootstrap --scope=user\n```\n\n\n## Bootstrap project using templates\n\n```bash\n$ flox bootstrap python                                                                                                                                                                                                                                                                            12:14:05\n → Create library project [y/N]: n\n → Python Version [3.8.12]:\n \n$ ls -la .\ndrwxr-xr-x   4 me  staff  128 Jan 13 11:54 .flox\ndrwxr-xr-x  13 me  staff  416 Jan 13 12:14 .git\n-rw-r--r--   1 me  staff    6 Jan 13 12:14 .python-version\n-rw-r--r--   1 me  staff   14 Jan 13 11:54 README.md\ndrwxr-xr-x   3 me  staff   96 Jan 13 11:54 flox_project\n-rw-r--r--   1 me  staff  454 Jan 13 12:14 pyproject.toml\n```\n\nflox templates may contain extra parameters which can be changed during bootstrap proces. \n\n\n## Template repository structure\n\nYou can create your own repository or fork default one https://github.com/getflox/flox-templates\nYour template repository should be structured like that:\n\n```\n.\n├── github-actions\n│         ├── hooks.py\n│         └── template\n├── python\n│         ├── template\n│         │         ├── <project_name_underscore>\n│         │         │         └── __init__.py\n│         │         └── pyproject.toml.j2\n│         └── variables.py\n└── serverless-python\n    ├── template\n    │         ├── package.json.j2\n    │         └── serverless.yml.py.j2\n    └── variables.py\n```\n\nWhere:\n\n- first level directory is a name of the template which can be passed as parameter to bootstrap command\n- `variables.py` is a simple python script containing one variable called `VARIABLES` which should be a list of `ParamDefinition` objects defining parameters\n- `hooks.py`  a simple script which may contain two functions `pre_install` and `post_install` which will be executed before and after bootstrap template is added to your project. \n additionally `pre_install` function will get all variables and all features installed for given project with the ability to filter template files which should be installed\n',
    'author': 'Michal Przytulski',
    'author_email': 'michal@przytulski.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/getflox/flox-bootstrap',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
