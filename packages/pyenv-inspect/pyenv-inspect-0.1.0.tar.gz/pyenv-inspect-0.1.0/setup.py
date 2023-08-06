# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyenv_inspect']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyenv-inspect',
    'version': '0.1.0',
    'description': 'An auxiliary library for the virtualenv-pyenv plugin',
    'long_description': '# pyenv-inspect\n\nAn auxiliary library for the [virtualenv-pyenv][virtualenv-pyenv] plugin\n\n## Limitations\n\nOnly CPython is supported at the moment.\n\n\n[virtualenv-pyenv]: https://github.com/un-def/virtualenv-pyenv\n',
    'author': 'un.def',
    'author_email': 'me@undef.im',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/un-def/pyenv-inspect',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
