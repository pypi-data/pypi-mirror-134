import socket
from typing import List

from vtrace import utils


def get_ip_address(hostname: str, port: int = 443) -> List[int]:
    """Gets the IP address given a valid hostname

    Uses socket.getaddrinfo
    https://docs.python.org/3/library/socket.html#socket.getaddrinfo"""

    if not utils.is_valid_hostname(hostname):
        raise ValueError(f"Hostname: {hostname} is not valid.")

    # Gets the address info for the given hostname/port/protocol combo
    # family=AF_INET -> ipv4
    # type=SOCK_STREAM -> tcp
    # port = 80/443 HTTP(S)
    address_list = socket.getaddrinfo(
        host=hostname,
        port=port,
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
    )

    # Returns only the ip address / port combo in the list
    address = list(map(lambda x: x[4], address_list))[0]

    # address -> (ip_addr, port) tuple
    return address[0]
