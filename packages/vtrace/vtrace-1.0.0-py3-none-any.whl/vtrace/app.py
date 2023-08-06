import os
import tempfile
import webbrowser

import click

from vtrace import dns, geo, traceroute, utils, mapper


@click.command()
@click.argument("target", nargs=1)
@click.option("-m", "--min-ttl", default=1, type=int)
@click.option("-M", "--max-ttl", default=64, type=int)
@click.option("-s", "--source-port", default=None, type=int)
@click.option("-d", "--destination-port", default=80, type=int)
@click.option("-t", "--timeout", default=3, type=int)
@click.option("-T", "--tcp", default=0, type=bool, is_flag=True)
@click.option("-I", "--icmp", default=0, type=bool, is_flag=True)
@click.option("-U", "--udp", default=0, type=bool, is_flag=True)
@click.option("--temp", default=0, type=bool, is_flag=True)
def main(
    target: str,
    min_ttl: int,
    max_ttl: int,
    source_port: int,
    destination_port: int,
    timeout: int,
    tcp: bool,
    icmp: bool,
    udp: bool,
    temp: bool,
) -> None:
    """Visually trace the route to a target"""

    if utils.is_valid_ipv4_address(target):
        ip_address = target
    else:
        ip_address = dns.get_ip_address(target)

    # Allow only one mode (TCP/UDP/ICMP)
    if len([x for x in [tcp, udp, icmp] if x]) > 1:
        raise ValueError("Can not combine TCP/UDP/ICMP flags (-T/-U/-I)")

    # Set the protocol based on the flag value, defaults to TCP_SYN
    if udp:
        protocol = traceroute.TraceRouteProtocol.UDP
    elif icmp:
        protocol = traceroute.TraceRouteProtocol.ICMP
    else:
        protocol = traceroute.TraceRouteProtocol.TCP_SYN

    # Perform the traceroute
    results = traceroute.traceroute(
        target_ip=ip_address,
        protocol=protocol,
        min_ttl=min_ttl,
        max_ttl=max_ttl,
        source_port=source_port,
        destination_port=destination_port,
        timeout=timeout,
    )

    # Creates the ipinfo.io geolocator service
    # If access_token is set to None, it will automatically try
    # to get the env var IP_INFO_ACCESS_TOKEN
    geolocator = geo.Geolocator(access_token=None)

    # Used to store a list of geolocation data for mapping purposes
    geolocation_list = []

    # Print output to CLI and retrieve geolocation data per ip adddress
    print(f"traceroute to {target} ({ip_address}), {max_ttl} hops max")
    for entry in results:
        print(f"{entry.ttl}\t{entry.ip}\t{entry.rtt:.2f}ms")

        # retrieve geolocation data per ip address
        geo_details = geolocator.geolocate(entry.ip)
        geolocation_list.append(geo_details)

    # Creates a map and saves it to a html file
    map = mapper.TraceRouteMap(geolocation_list)

    # Save the generated HTML map to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as fp:
        file_location = fp.name

        # Save the file to html
        map.save(file_location)

        # Grant permissions
        os.chmod(file_location, 0o755)

        # If a browser is available open the map in the browser
        webbrowser.open(f"file://{file_location}")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
