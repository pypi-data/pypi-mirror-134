import folium

from vtrace import geo
from typing import List
from dataclasses import dataclass


@dataclass
class Coordinate:
    latitude: float
    longitude: float


class TraceRouteMap(folium.Map):
    """Extends the Folium Map with traceroute markers"""

    def __init__(self, geolocation_list: List[geo.GeoLocationDetails], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.path = []

        for geolocation in geolocation_list:
            # Some coords can be none (e.g. local IP)
            if geolocation.latitude and geolocation.longitude:

                coordinate = Coordinate(
                    float(geolocation.latitude), float(geolocation.longitude)
                )

                # Add the coords to a path
                self.path.append(coordinate)

                # Add the marker to the map
                text = f"IP address: {geolocation.ip}"
                self.add_marker(coordinate, text)

        # Generate a path through all traceroute coords
        self.add_line(self.path, 3)

        # Set the zoom levels
        self.fit_bounds(self.get_bounds(), padding=(30, 30))

    def add_marker(self, coordinate: Coordinate, text: str) -> None:
        """Adds a marker with text to the folium map at 'Coordinate'"""

        # Extract the coordinate in a tuple
        location = (coordinate.latitude, coordinate.longitude)

        # Creates the marker object
        marker = folium.Marker(
            location=location,
            popup=text,
        )

        # Add the marker to the map
        marker.add_to(self)

    def add_line(self, location_list: Coordinate, weight: int) -> None:
        """Adds a PolyLine to the Folium Map"""

        # converts List[Coordinate] -> List[Tuple[float, float]]
        locations = list(map(lambda x: (x.latitude, x.longitude), location_list))

        # Creates a line representation between all coordinates
        line = folium.PolyLine(locations=locations, weight=weight)

        # Adds the line to the map
        line.add_to(self)
