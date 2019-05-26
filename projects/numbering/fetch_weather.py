"""
Fetch Current Weather - Get the current weather for a given zip/postal code. Optional: Try
locating the user automatically.
"""
# noinspection PyCompatibility
from urllib import request
import json


def get_ip():
    """
    :return:
    """
    url = "http://checkip.dyndns.org"
    data = request.urlopen(url).read()
    ip_address = data[-30:-16]
    return ip_address


def get_weather(ip_address):
    """
    :param ip_address:
    :return:
    """
    end_point = "http://api.worldweatheronline.com/free/v1/weather.ashx?"
    # noinspection SpellCheckingInspection
    query = "key=a37fae643df77aa83d88abbc9e8e96194ab242d4&q=" + \
            str(ip_address) + "&num_of_days=0&format=json"
    url = end_point + query
    json_data = request.urlopen(url).read()
    data = json.loads(json_data)
    current_weather = data['data']['current_condition'][0]
    return current_weather


def print_weather(data):
    """
    :param data:
    """
    # noinspection SpellCheckingInspection
    print("""
    Weather : %s 
    Temperatue : %s Celsius
    Wind : %s Kmph %s 
    Humidity : %s 
    Precipitation : %s MM
    """ % (data['weatherDesc'][0]['value'],
           data['temp_C'],
           data['windspeedKmph'], data['winddir16Point'], data['humidity'], data['precipMM'])
          )


def main():
    """main"""
    print("\nGetting weather information for your location...")
    ip_address = get_ip()
    data = get_weather(ip_address)
    print_weather(data)


if __name__ == "__main__":
    main()
