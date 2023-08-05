# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reflectionist']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0', 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['reflectionist = reflectionist.cli:app']}

setup_kwargs = {
    'name': 'reflectionist',
    'version': '0.1.2',
    'description': 'A simple CLI app that helps you to track your reflections during your day.',
    'long_description': "\n# reflectionist\n\nA simple CLI app that helps you to track your reflections during your day.\n\n\n# Why?\nBeing capable of reflecting helps to understand stressful situations.\n\nHaving a different perspective on what happened facilitates to take actions on how to behave to avoid the same feeling again reducing your stress levels and enabling personal growth!\n\n## Reflection questions\n\nThe following questions were extracted from my experience at Hyper Island, during the master's in Digital Management.\n\n\n    1. What happened that affected me?\n    2. How did I feel then and now?\n    3. What did I learn about myself?\n\n\n\n\n## Installation\n\nInstall reflectionist with pip\n\n```bash\n  pip install reflectionist\n```\n    \n## Features\n\n- Init environment: `reflectionist init`\n- Add reflection: `reflectionist create`\n- List reflections: `reflectionist list`\n- Describe specific reflection: `reflectionist describe`\n\n\n## Contributing\n\nContributions are always welcome! Just open a new issue that I will check it ASAP.\n\n",
    'author': 'Dênis Araújo da Silva',
    'author_email': 'silvadenisaraujo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
