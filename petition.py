import json
import requests
from LatLong import LatLong

class PlacePetition:
    city = None
    state = None
    country = None
    # api url, it will be formate
    __url__ = "http://www.datasciencetoolkit.org/coordinates2politics/{lat}%2c{long}"
    def __init__(self, location:LatLong):
        self.location = location
        # start the petition
        self.__start_petition__()

    def __start_petition__(self):
        """
        make the petition from the api server
        """
        url = self.__url__.format(lat=self.location.get_lat(), long=self.location.get_long())
        # make the request
        with requests.get(url) as r:
            # parse the data to json object
            data = json.loads(r.text)[0]
            # if server return an eror
            if "error" in data.keys():
                raise ValueError(data["error"])
            if "politics" in data.keys():
                locations = data["politics"]
                if locations != "null": # if have samething in locations:
                    for l in locations:
                        if "country" == l["friendly_type"]:
                            self.country = l["name"]
                        elif "state" == l["friendly_type"]:
                            self.state = l["name"]
                        elif "city" == l["friendly_type"]:
                            self.city = l["name"]
            r.close()

    def __str__(self):
        return "{}, {} {}".format(self.country, self.state, self.city)

    def get_json(self):
        """
        :return: json object with all information
        """
        son = {
            "country": self.country,
            "state" : self.state,
            "city": "null" if self.city == None else self.city,
            "lat": self.location.get_lat(),
            "long": self.location.get_long()
        }
        return json.dumps(son);

