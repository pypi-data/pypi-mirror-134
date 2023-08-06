# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vtrace']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0',
 'folium>=0.12.1,<0.13.0',
 'ipinfo>=4.2.1,<5.0.0',
 'scapy>=2.4.5,<3.0.0']

entry_points = \
{'console_scripts': ['vtrace = vtrace.app:main']}

setup_kwargs = {
    'name': 'vtrace',
    'version': '1.0.0',
    'description': 'A command line application to trace the route to a host and provide the user with a visual map.',
    'long_description': '# VTrace - Visualize traceroutes 🚀\n\n[![codecov](https://codecov.io/gh/RichardBieringa/vtrace/branch/master/graph/badge.svg?token=RB6Y7SZ1FC)](https://codecov.io/gh/RichardBieringa/vtrace)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## Description\nMimicks a primitive version of [GNU traceroute](https://linux.die.net/man/8/traceroute) while providing a visual map of the route in the browser! \n\n![Example Traceroute](example/terminal.png)\n![Example Map](example/map.png)\n\n## Installation\n\nInstall using pip\n```sh\n$ pip install vtrace\n```\n\n## Usage\n\n⚠️ **Warning:** requires elevated priviledges ⚠️\n\n```sh\n# vtrace google.com\n```\n\nFor help run \n```sh\n$ vtrace --help\n```\n\n## Tools used\n\n| Plugin | README |\n| ------ | ------ |\n| [Scapy](https://scapy.net/) | For creating/sending network packets to implement traceroute functionalities.  |\n| [IPInfo](https://ipinfo.io/) | Geolocation service to get the coordinates of IP addresses.  |\n| [Folium](https://python-visualization.github.io/folium/) | To implement the visual mapping. |\n| [Click](https://click.palletsprojects.com/en/8.0.x/) | To create the command line interface. |\n\n',
    'author': 'Richard Bieringa',
    'author_email': 'richardbieringa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/RichardBieringa/vtrace',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
