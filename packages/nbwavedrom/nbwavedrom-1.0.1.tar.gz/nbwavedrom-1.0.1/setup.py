# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nbwavedrom']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'nbwavedrom',
    'version': '1.0.1',
    'description': 'Wavedrom timing diagrams for Jupyter Notebook',
    'long_description': 'nbwavedrom\n==========\n\nA simple package to add wavedrom (http://wavedrom.com) timing diagrams into a jupyter notebook.\n\nExample: https://github.com/witchard/nbwavedrom/blob/master/examples/example.ipynb.\n\nTo get started simply `pip install nbwavedrom` or `pip install git+git://github.com/witchard/nbwavedrom.git`\nfor the development version. Then take a look at the example notebook within jupyter notebook.\n\nThe waveforms are rendered using the wavedrom-cli. Installation instructions can be found here: https://github.com/wavedrom/cli/.\n',
    'author': 'witchard',
    'author_email': 'witchard@hotmail.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/witchard/nbwavedrom',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
