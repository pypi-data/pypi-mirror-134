# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ah_blackjack']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.4,<0.5.0', 'names>=0.3.0,<0.4.0']

entry_points = \
{'console_scripts': ['bj = ah_blackjack.main:main']}

setup_kwargs = {
    'name': 'ah-blackjack',
    'version': '0.1.4',
    'description': 'Black jack in terminal',
    'long_description': '# Belhard Projects\n\n## BlackJack\nSimple **black jack** game in terminal.\n\n[![asciicast](https://asciinema.org/a/u5pClKzpWHrvZFRQqVqYnwfMc.svg)](https://asciinema.org/a/u5pClKzpWHrvZFRQqVqYnwfMc)\n\nInstall:\n```shell\npip3 install ah-blackjack\n```\nExecute:\n```shell\nbj\n```\n\n<details>\n\n<summary>others</summary>\n- WallPapper Calculator\n- Backet Of Water\n</details>\n',
    'author': 'Andrew Horbach',
    'author_email': 'andrewhorbach@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/karma-git/belhard_base_python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
