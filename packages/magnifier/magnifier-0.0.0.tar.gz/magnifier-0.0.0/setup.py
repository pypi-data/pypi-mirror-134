# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magnifier', 'magnifier.evaluation', 'magnifier.transformer']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0',
 'mlflow>=1.22.0,<2.0.0',
 'numpy>=1.20.0,<2.0.0',
 'pandas>=1.1.4,<2.0.0',
 'pydub>=0.25.1,<0.26.0',
 'python_speech_features>=0.6,<0.7',
 'scikit-learn>=1.0.2,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'typing-extensions>=4.0.1,<5.0.0']

setup_kwargs = {
    'name': 'magnifier',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'koreander2001',
    'author_email': 'neokamiyama@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
