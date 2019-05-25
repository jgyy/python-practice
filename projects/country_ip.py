"""
Country from IP Lookup - Enter an IP address and find the country that IP is registered in.
Optional: Find the Ip automatically.
"""
# noinspection PyCompatibility
from urllib import request
import json
import re


def get_public_ip():
    """
    :return: Get Public IP
    """
    ip_data = str(request.urlopen('http://checkip.dyndns.com/').read())
    # noinspection RegExpAnonymousGroup
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(ip_data).group(1)


if __name__ == '__main__':
    IP = str(get_public_ip())

    # Get Location
    URL = 'http://ipinfo.io/' + IP + '/json'
    RESPONSE = request.urlopen(URL)
    DATA = json.load(RESPONSE)
    CITY = DATA['city']
    REGION = DATA['region']
    COUNTRY = DATA['country']
    LOCATION = DATA['loc']
    ORG = DATA['org']

    # Print Extracted Details
    print("Your City : " + CITY)
    print("Your Region : " + REGION)
    print("Your Country : " + COUNTRY)
    print("Your Location : " + LOCATION)
