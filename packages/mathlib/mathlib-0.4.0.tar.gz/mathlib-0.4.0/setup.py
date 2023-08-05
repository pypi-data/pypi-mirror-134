# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mathlib']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mathlib',
    'version': '0.4.0',
    'description': 'A pure-python maths library',
    'long_description': '====================================\nmathlib: a pure python maths library\n====================================\n\n.. image:: https://github.com/spapanik/mathlib/actions/workflows/build.yml/badge.svg\n  :alt: Build\n  :target: https://github.com/spapanik/mathlib/actions/workflows/build.yml\n.. image:: https://img.shields.io/lgtm/alerts/g/spapanik/mathlib.svg\n  :alt: Total alerts\n  :target: https://lgtm.com/projects/g/spapanik/mathlib/alerts/\n.. image:: https://img.shields.io/github/license/spapanik/mathlib\n  :alt: License\n  :target: https://github.com/spapanik/mathlib/blob/main/LICENSE.txt\n.. image:: https://img.shields.io/pypi/v/mathlib\n  :alt: PyPI\n  :target: https://pypi.org/project/mathlib\n.. image:: https://pepy.tech/badge/mathlib\n  :alt: Downloads\n  :target: https://pepy.tech/project/mathlib\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n  :alt: Code style\n  :target: https://github.com/psf/black\n\n``mathlib`` is a maths library written in pure python, so that it can be used\n\nIn a nutshell\n-------------\n\nInstallation\n^^^^^^^^^^^^\n\nThe easiest way is to use `poetry`_ to manage your dependencies and add *mathlib* to them.\n\n.. code-block:: toml\n\n    [tool.poetry.dependencies]\n    mathlib = "^0.4.0"\n\nUsage\n^^^^^\n\n``mathlib`` mainly offers some number theoretic functions.\n\n\nLinks\n-----\n\n- `Documentation`_\n- `Changelog`_\n\n\n.. _poetry: https://python-poetry.org/\n.. _Changelog: https://github.com/spapanik/mathlib/blob/main/CHANGELOG.rst\n.. _Documentation: https://mathlib.readthedocs.io/en/latest/\n',
    'author': 'Stephanos Kuma',
    'author_email': 'stephanos@kuma.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/spapanik/mathlib',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
