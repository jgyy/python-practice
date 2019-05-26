"""
Fortune Teller (Horoscope) - A program that checks your horoscope on various astrology sites and
puts them together for you each day.
"""
import sys
# noinspection PyCompatibility
import urllib.request as ur
from bs4 import BeautifulSoup


def horoscope(sign):
    """
    :param sign:
    """
    url = 'http://my.horoscope.com/astrology/free-daily-horoscope-%s.html' % sign
    html_doc = ur.urlopen(url)
    soup = BeautifulSoup(html_doc.read(), features="lxml")
    text = soup.find_all(id="textline")[1].get_text()
    date = soup.find_all(id='advert')[1].get_text()
    print("%s - %s\n\n%s" % (sign.capitalize(), date, text))


if __name__ == '__main__':
    try:
        horoscope(sys.argv[1])
    except IndexError:
        print("Please enter a valid zodiac sign.\nUsage example: python horoscope.py taurus")
