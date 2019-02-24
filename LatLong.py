
class LatLong:
    """
    Representate a coordenate position
    """
    def __init__(self, latitude, longitude):
        self.__latitude__ = latitude;
        self.__longitude__ = longitude;

    def get_lat(self):
        """

        :return: the latitude
        """
        return self.__latitude__

    def get_long(self):
        """

        :return: the longitude
        """
        return self.__longitude__

    def __str__(self):
        return "({},{})".format(self.__latitude__, self.__longitude__)

    def __add__(self, other):
        if type(other) != type(self):
            return;
        else:
            lng = self.__longitude__ + other.get_long()
            lat = self.__latitude__ + other.get_lat()
            return LatLong(lat, lng)