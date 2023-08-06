import os
import ipinfo

from typing import Optional
from dataclasses import dataclass

try:
    import dotenv

    dotenv.load_dotenv()
except ImportError:
    pass


@dataclass
class GeoLocationDetails:
    """Represents the geolocation details returned from ipinfo.io"""

    # Stuff thats always there
    bogon: bool = False
    ip: str = "0.0.0.0"
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    country_name: Optional[str] = None

    # Only non "bogon" ip addresses have these properties
    hostname: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    loc: Optional[str] = None
    org: Optional[str] = None
    postal: Optional[str] = None
    timezone: Optional[str] = None
    readme: Optional[str] = None
    anycast: Optional[str] = None


class Geolocator:
    """Allows the user to look up geolocation info from an IP address"""

    def __init__(self, access_token: Optional[str] = None) -> None:
        # Fetch access_token from environment variables if unspecified
        if not access_token:
            access_token = os.environ.get("IP_INFO_ACCESS_TOKEN")

        self.access_token = access_token
        self.handler = ipinfo.getHandler(access_token)

    def geolocate(self, ip_address: str, timeout: int = 2) -> GeoLocationDetails:
        """Synchronously request geolocation details for an IP address"""

        # The result from the ipinfo.io api
        result = self.handler.getDetails(ip_address, timeout)

        # Unpack it into our custom data class
        location_details = GeoLocationDetails(**result.details)

        return location_details
