"""
Work out the distance (user specified units) given two cities using haversine equation
"""

import sys
from pygeocoder import Geocoder
import numpy as np


def get_distance(loc_a, loc_b):
    """
    :param loc_a:
    :param loc_b:
    :return: returns calculated haversine formula
    """
    earth_rad = 6371.0
    d_lat = np.deg2rad(loc_b[0] - loc_a[0])
    d_lon = np.deg2rad(loc_b[1] - loc_a[1])
    l_a = np.sin(d_lat / 2) * np.sin(d_lat / 2) + \
        np.cos(np.deg2rad(loc_a[0])) * np.cos(np.deg2rad(loc_b[0])) * \
        np.sin(d_lon / 2) * np.sin(d_lon / 2)
    l_c = 2 * np.arctan2(np.sqrt(l_a), np.sqrt(1 - l_a))
    return earth_rad * l_c


def get_lat_longs(location):
    """
    :param location:
    :return:
    """
    geocode = Geocoder()
    return geocode.geocode(location)[0].coordinates


def convert_km_to_miles(kilo_meter):
    """
    :param kilo_meter:
    :return:
    """
    miles_per_km = 0.621371192
    return kilo_meter * miles_per_km


def main():
    """get first city, then get second city"""
    print('Type the first City: ')
    city_a = input()

    print('Type the second city: ')
    city_b = input()

    # get units
    units = ''
    while (units != 'k') & (units != 'm'):
        print('Type distance units (miles or kilometers): ')
        units = str.lower(input())
        if units in ['clicks', 'km', 'kilometers', 'kilometer', 'k']:
            units = 'km'
        elif units in ['m', 'mile', 'miles']:
            units = 'm'
        else:
            print('units not recognised, please try again')

    # find the distance in km
    try:
        distance = get_distance(get_lat_longs(city_a),
                                get_lat_longs(city_b))
        # display the distance
        if units == 'km':
            print(str(distance), ' km')
        else:
            distance = convert_km_to_miles(distance)
            print(str(distance), ' miles')

    except AssertionError:
        print('Error raised.  Are the input cities correct?')


if __name__ == '__main__':
    sys.exit(main())
