from math import radians, sin, cos, sqrt, atan2
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def haversine(coord1, coord2):
    R = 6371.0

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def get_location_name(geolocator, coordinates):
    try:
        location = geolocator.reverse(coordinates, exactly_one=True, language='en')
        if location:
            address = location.raw.get('address', {})
            city = address.get('city', '')
            town = address.get('town', '')
            village = address.get('village', '')
            island = address.get('island', '')

            if city:
                return city
            elif town:
                return town
            elif village:
                return village
            elif island:
                return island
            else:
                return location.address.split(",")[0]
    except GeocoderTimedOut:
        print(f"GeocoderTimedOut: Could not get location for  {coordinates}")
        return "unknown_location"
    except Exception as e:
        print(f"Error in get_location_name: {e}")
        return "unknown_location"
