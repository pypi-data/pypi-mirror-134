# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['palindrome_tree']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3.5,<2.0.0',
 'requests>=2.26.0,<3.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'xgboost>=1.5.1,<2.0.0']

setup_kwargs = {
    'name': 'palindrome-tree',
    'version': '0.0.13',
    'description': 'Gradient boosted decision tree palindrome predictor, used to locate regions for further investigation thru http://palindromes.ibp.cz/',
    'long_description': None,
    'author': 'patrik.kaura',
    'author_email': '160702@vutbr.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
