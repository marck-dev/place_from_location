
class LatLong:
    """
    Representate a coordenate position
    """
    def __init__(self, latitude, longitude):
        self.latitude = latitude;
        self.longitude = longitude;

    def get_lat(self):
        """

        :return: the latitude
        """
        return self.latitude

    def get_long(self):
        """

        :return: the longitude
        """
        return self.longitude

    def __str__(self):
        return "({},{})".format(self.latitude, self.longitude)

    def __add__(self, other):
        if type(other) != type(self):
            return;
        else:
            lng = self.longitude + other.get_long()
            lat = self.latitude + other.get_lat()
            return LatLong(lat, lng)