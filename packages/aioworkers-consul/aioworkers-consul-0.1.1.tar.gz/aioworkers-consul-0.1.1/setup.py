# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioworkers_consul']

package_data = \
{'': ['*']}

install_requires = \
['aioworkers>=0.19']

setup_kwargs = {
    'name': 'aioworkers-consul',
    'version': '0.1.1',
    'description': '',
    'long_description': 'aioworkers-consul\n=================\n\n.. image:: https://img.shields.io/pypi/v/aioworkers-consul.svg\n  :target: https://pypi.org/project/aioworkers-consul\n  :alt: PyPI version\n\n.. image:: https://img.shields.io/pypi/pyversions/aioworkers-consul.svg\n  :target: https://pypi.org/project/aioworkers-consul\n  :alt: Python versions\n\nAbout\n=====\n\nIntegration with `Hashicorp Consul <https://www.consul.io>`_.\n\nUse\n---\n\n.. code-block:: yaml\n\n    consul:\n      host: localhost:8500  # optional\n      service:              # optional\n        name: my\n        tags:\n          - worker\n\n\nDevelopment\n-----------\n\nInstall dev requirements:\n\n\n.. code-block:: shell\n\n    poetry install\n\n\nRun linters:\n\n.. code-block:: shell\n\n    make\n',
    'author': 'Alexander Malev',
    'author_email': 'malev@somedev.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aioworkers/aioworkers-consul',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
