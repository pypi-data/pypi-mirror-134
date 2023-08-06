import enum
import logging
from dataclasses import dataclass, field
from typing import List

from scapy import sendrecv
from scapy.layers import inet


@dataclass(order=True)
class TraceRouteResult:
    """Represents the return value of the traceroute command"""

    sort_index: int = field(init=False, repr=False)

    ttl: int = 0
    ip: str = "0.0.0.0"
    rtt: float = 0

    def __post_init__(self):
        """Allows for sorting based on TraceRouteResult.ttl"""
        object.__setattr__(self, "sort_index", self.ttl)


class TraceRouteProtocol(enum.Enum):
    """Represents the types of traceroute requests the user can make"""

    TCP_SYN = enum.auto()
    ICMP = enum.auto()
    UDP = enum.auto()
    DNS = enum.auto()


def traceroute(
    target_ip: str,
    protocol: TraceRouteProtocol = TraceRouteProtocol.TCP_SYN,
    min_ttl: int = 1,
    max_ttl: int = 64,
    source_port: int = None,
    destination_port: int = 80,
    timeout: int = 3,
    verbose: bool = False,
) -> List[TraceRouteResult]:
    """Performs a traceroute request to the given host"""
    logging.info("Traceroute::traceroute(%s)", target_ip)

    # Generates a random port to send the packet from
    if source_port is None:
        source_port = inet.RandShort()

    packet = None
    match protocol:

        # TCP_SYN protocol
        case TraceRouteProtocol.TCP_SYN:
            packet = inet.IP(
                dst=target_ip, id=inet.RandShort(), ttl=(min_ttl, max_ttl)
            ) / inet.TCP(dport=destination_port, sport=source_port, flags="S")

        # ICMP protocol
        case TraceRouteProtocol.ICMP:
            packet = inet.IP(
                dst=target_ip, id=inet.RandShort(), ttl=(min_ttl, max_ttl)
            ) / inet.ICMP(id=inet.RandShort())

        # UDP based traceroute
        case TraceRouteProtocol.UDP:
            raise NotImplementedError("Protocol not implemented")

        case _:
            raise NotImplementedError("Protocol not implemented")

    # Sends and receives packets
    ans, _ = sendrecv.sr(packet, timeout=timeout, verbose=verbose)

    seen = {}
    results = []
    for send, receive in ans:
        # Prevent duplicate entries
        if receive.src not in seen:

            # Add it to the hash map to prevent duplicates
            seen[receive.src] = True

            # Calculates the Round-Trip-Time in miliseconds
            rtt = (receive.time - send.sent_time) * 1000

            entry = TraceRouteResult(send.ttl, receive.src, rtt)
            results.append(entry)

    # Sorts the results based on the TTL value
    results.sort()

    return results
