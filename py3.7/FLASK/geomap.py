from geopy.geocoders import Nominatim

class GeoMap:
    def __init__(self, app_name, city, state):
        self.app_name = app_name
        self.city = city
        self.state = state

    def get_geotag(self):
        geolocator = Nominatim(user_agent=self.app_name)
        location = geolocator.geocode(f"{self.city}, {self.state}")
        try:
            return location.latitude, location.longitude
        except AttributeError:
            return 'none', 'none'