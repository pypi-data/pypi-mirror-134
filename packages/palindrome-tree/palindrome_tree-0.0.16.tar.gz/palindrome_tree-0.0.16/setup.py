# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['palindrome_tree']

package_data = \
{'': ['*'], 'palindrome_tree': ['model/*']}

install_requires = \
['pandas>=1.3.5,<2.0.0',
 'requests>=2.26.0,<3.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'xgboost>=1.5.1,<2.0.0']

setup_kwargs = {
    'name': 'palindrome-tree',
    'version': '0.0.16',
    'description': 'Gradient boosted decision tree palindrome predictor, used to locate regions for further investigation thru http://palindromes.ibp.cz/',
    'long_description': '# Palindrome tree\n\nPalindrome tree tool is used for analyzing inverted repeats in various DNA sequences using decision trees. This tool takes provided sequences and finds interesting parts in which there\'s high probability of palindrome occurrence using decision tree. This process filters a big portion of data. Interesting data are then analyzed using API from [Palindrome Analyzer](http://dx.doi.org/10.1016/j.bbrc.2016.09.015). DNA Analyser is a web-based server for nucleotide sequence analysis. It has been developed thanks to cooperation of Department of Informatics, Mendel’s University in Brno and Institute of Biophysics, Academy of Sciences of the Czech Republic. \n\n## Requirements\n\nPalindrome tree was built with Python 3.7+.\n\n## Installation\n\nDescription of installation\n\n## Usage\n\nDescription of usage\n\n## Dependencies\n\n* xgboost = "^1.5.1"\n* pandas = "^1.3.5"\n* scikit-learn = "^1.0.2"\n* requests = "^2.26.0"\n\n## Authors\n\n* **Jaromir Kratochvil** - *Main developer* - [jaromirkratochvil](\nhttps://github.com/kratjar\n)\n\n* **Patrik Kaura** - *Developer* - [patrikkaura](\nhttps://gitlab.com/PatrikKaura/\n)\n\n* **Jiří Šťastný** - *Supervisor*\n\n## License\n\nThis project is licensed under the MIT License - see the [\nLICENSE\n](\nLICENSE\n) file for details. \n\n',
    'author': 'jaromir.kratochvil',
    'author_email': '171433@vutbr.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/patrikkaura/palindrome-tree',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
