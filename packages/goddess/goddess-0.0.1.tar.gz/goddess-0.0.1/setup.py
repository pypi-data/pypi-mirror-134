# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gaea']

package_data = \
{'': ['*']}

install_requires = \
['PySide6>=6.2.2,<7.0.0', 'canopy-platform>=0,<1', 'understory>=0,<1']

setup_kwargs = {
    'name': 'goddess',
    'version': '0.0.1',
    'description': 'Spawn your personal website.',
    'long_description': '# Gaea\n\nSpawn your personal website.\n\n## Use\n\n### Binary Executables\n\nLinux x64 | Windows | OS X\n\n### Source Installation\n\n    pip install goddess\n\n## Develop\n\n### Try/Test\n\n    git clone https://github.com/canopy/gaea.git && cd gaea\n    poetry install\n    poetry run python -m gaea\n\n### Build\n\n    poetry run python build.py ( linux | macos | windows )\n    ./dist/gaea [ port ]\n',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
