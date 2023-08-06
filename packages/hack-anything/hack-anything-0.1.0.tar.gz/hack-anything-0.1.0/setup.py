# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hack_anything']

package_data = \
{'': ['*']}

install_requires = \
['tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'hack-anything',
    'version': '0.1.0',
    'description': '',
    'long_description': '\n# hack_anything\n\nAn efficient and robust library to hack anything.\n\n\n## Installation\n\nInstall project with pip\n\n```bash\n  pip install hack_anything  \n```\n    \n## Usage/Examples\n\n```python\nfrom hack_anything import hack_tool\n\nhack_tool.hack("Universal.Co")\n\n```\n\n',
    'author': 'Praneeth',
    'author_email': 'spraneeth4@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
