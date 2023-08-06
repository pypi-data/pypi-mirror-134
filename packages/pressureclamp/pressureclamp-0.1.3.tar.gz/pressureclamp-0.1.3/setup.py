# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pressureclamp']

package_data = \
{'': ['*']}

install_requires = \
['cufflinks>=0.17.3,<0.18.0',
 'numpy>=1.22.1,<2.0.0',
 'pandas>=1.3.5,<2.0.0',
 'plotly>=5.5.0,<6.0.0',
 'scipy>=1.7.3,<2.0.0']

setup_kwargs = {
    'name': 'pressureclamp',
    'version': '0.1.3',
    'description': 'A package for analyzing pressure clamp electrophysiology data acquired in HEKA patchmaster.',
    'long_description': None,
    'author': 'Michael Young',
    'author_email': 'neuromyoung@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/neuro-myoung/pressureclamp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
