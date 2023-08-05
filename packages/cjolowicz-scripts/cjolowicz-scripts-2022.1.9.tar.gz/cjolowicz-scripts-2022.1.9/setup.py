# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cjolowicz_scripts']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0',
 'Pygments>=2.10.0',
 'click>=8.0.1',
 'github3.py>=3.0.0',
 'httpx>=0.21.1',
 'matplotlib>=3.5.0',
 'platformdirs>=2.4.0',
 'rich>=10.15.2']

entry_points = \
{'console_scripts': ['compare-tools = cjolowicz_scripts.compare_tools:main',
                     'dependabot-rebase-all = '
                     'cjolowicz_scripts.dependabot_rebase_all:main',
                     'mbox2maildir = cjolowicz_scripts.mbox2maildir:main',
                     'pypi-dependents = cjolowicz_scripts.pypi_dependents:main',
                     'python-stdlib = cjolowicz_scripts.python_stdlib:main',
                     'stardate = cjolowicz_scripts.stardate:main',
                     'yaml2json = cjolowicz_scripts.yaml2json:main']}

setup_kwargs = {
    'name': 'cjolowicz-scripts',
    'version': '2022.1.9',
    'description': 'Miscellaneous Python scripts',
    'long_description': "Miscellaneous Python scripts\n============================\n\n|PyPI| |Status| |Python Version| |License| |Read the Docs| |Tests| |Codecov|\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/cjolowicz-scripts.svg\n   :target: https://pypi.org/project/cjolowicz-scripts/\n   :alt: PyPI\n.. |Status| image:: https://img.shields.io/pypi/status/cjolowicz-scripts.svg\n   :target: https://pypi.org/project/cjolowicz-scripts/\n   :alt: Status\n.. |Python Version| image:: https://img.shields.io/pypi/pyversions/cjolowicz-scripts\n   :target: https://pypi.org/project/cjolowicz-scripts\n   :alt: Python Version\n.. |License| image:: https://img.shields.io/pypi/l/cjolowicz-scripts\n   :target: https://opensource.org/licenses/MIT\n   :alt: License\n.. |Read the Docs| image:: https://img.shields.io/readthedocs/cjolowicz-scripts/latest.svg?label=Read%20the%20Docs\n   :target: https://cjolowicz-scripts.readthedocs.io/\n   :alt: Read the documentation at https://cjolowicz-scripts.readthedocs.io/\n.. |Tests| image:: https://github.com/cjolowicz/python-scripts/workflows/Tests/badge.svg\n   :target: https://github.com/cjolowicz/python-scripts/actions?workflow=Tests\n   :alt: Tests\n.. |Codecov| image:: https://codecov.io/gh/cjolowicz/cjolowicz-scripts/branch/main/graph/badge.svg\n   :target: https://codecov.io/gh/cjolowicz/cjolowicz-scripts\n   :alt: Codecov\n\n\nWelcome to my assortment of random Python scripts,\nall of which come with no guarantees whatsoever.\n\n\nInstallation\n------------\n\nYou can install these scripts via pip_ from PyPI_:\n\n.. code:: console\n\n   $ pip install cjolowicz-scripts\n\n\nUsage\n-----\n\nPlease see the Documentation_ for details.\n\n\nContributing\n------------\n\nContributions are very welcome.\nTo learn more, see the `Contributor Guide`_.\n\n\nLicense\n-------\n\nDistributed under the terms of the `MIT license`_,\nthese scripts are free and open source software.\n\n\nIssues\n------\n\nIf you encounter any problems,\nplease `file an issue`_ along with a detailed description.\n\n\nCredits\n-------\n\nThis project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.\n\n.. _@cjolowicz: https://github.com/cjolowicz\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _MIT license: https://opensource.org/licenses/MIT\n.. _PyPI: https://pypi.org/\n.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n.. _file an issue: https://github.com/cjolowicz/python-scripts/issues\n.. _pip: https://pip.pypa.io/\n.. github-only\n.. _Contributor Guide: CONTRIBUTING.rst\n.. _Documentation: https://cjolowicz-scripts.readthedocs.io/\n",
    'author': 'Claudio Jolowicz',
    'author_email': 'mail@claudiojolowicz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cjolowicz/python-scripts',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
