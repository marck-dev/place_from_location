import argparse
from petition import PlacePetition
from lat_long import LatLong

program_name = "Place From Location"
desc = "Get the location info as places"

parser = argparse.ArgumentParser(prog=program_name, description=desc)
parser.add_argument("-lat", help="Location latitude", required=True)
parser.add_argument("-long", help="Location longitude", required=True)
args = parser.parse_args()
loc = LatLong(args.lat, args.long)
place = PlacePetition( loc )
print( 'City: ', place.city if place.city is not None else "")
print( "State: ", place.state if place.state is not None else "")
print( "Country: ", place.country if place.country is not None else "")
print("Location: {}, {}".format(place.location.get_lat(), place.location.get_long()))


def getPlace( loc:LatLong ):
    """

    :param loc: LatLong object thar represent the location
    :return: json with all information
    """
    return PlacePetition(loc).get_json()