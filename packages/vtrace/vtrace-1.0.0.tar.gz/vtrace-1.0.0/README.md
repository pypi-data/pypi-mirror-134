# VTrace - Visualize traceroutes 🚀

[![codecov](https://codecov.io/gh/RichardBieringa/vtrace/branch/master/graph/badge.svg?token=RB6Y7SZ1FC)](https://codecov.io/gh/RichardBieringa/vtrace)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Description
Mimicks a primitive version of [GNU traceroute](https://linux.die.net/man/8/traceroute) while providing a visual map of the route in the browser! 

![Example Traceroute](example/terminal.png)
![Example Map](example/map.png)

## Installation

Install using pip
```sh
$ pip install vtrace
```

## Usage

⚠️ **Warning:** requires elevated priviledges ⚠️

```sh
# vtrace google.com
```

For help run 
```sh
$ vtrace --help
```

## Tools used

| Plugin | README |
| ------ | ------ |
| [Scapy](https://scapy.net/) | For creating/sending network packets to implement traceroute functionalities.  |
| [IPInfo](https://ipinfo.io/) | Geolocation service to get the coordinates of IP addresses.  |
| [Folium](https://python-visualization.github.io/folium/) | To implement the visual mapping. |
| [Click](https://click.palletsprojects.com/en/8.0.x/) | To create the command line interface. |

