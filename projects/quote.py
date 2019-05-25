"""
Quote Tracker (market symbols etc) - A program which can go out and check the current value of
stocks for a list of symbols entered by the user. The user can set how often the stocks are
checked. For CLI, show whether the stock has moved up or down. Optional: If GUI, the program
can show green up and red down arrows to show which direction the stock value has moved.
"""
import argparse
import time
# noinspection PyCompatibility
import urllib.request

from xml.etree.ElementTree import fromstring


def check_negative(value):
    """
    :param value:
    :return:
    """
    err_msg = "Interval {} is an invalid positive int value".format(value)
    try:
        ret_value = int(value)
    except TypeError:
        raise argparse.ArgumentTypeError(err_msg)

    if ret_value < 0:
        raise argparse.ArgumentTypeError(err_msg)

    return ret_value


def get_stock_value(symbol):
    """
    :param symbol:
    :return:
    """
    url = "http://dev.markitondemand.com/Api/v2/Quote/xml?symbol={}".format(symbol)
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    try:
        req = urllib.request.Request(url, headers)
        data = urllib.request.urlopen(req)
        xml_root = fromstring(data.read())

        if xml_root.tag != "StockQuote":
            print("Company {} not found".format(symbol))
            return None

        xml_dict = {child.tag: child.text for child in xml_root}

        if xml_dict.get('Status') in (None, not 'SUCCESS'):
            print("Corrupted Data")
            return None

        if xml_dict.get('LastPrice') is None or xml_dict.get('Name') is None:
            print("Corrupted Data")
            return None
        return [xml_dict.get('Name'), float(xml_dict.get('LastPrice'))]
    except TypeError:
        print("Corrupted Data")
        return None


if __name__ == '__main__':

    MIN_INTERVAL = 30
    DEF_INTERVAL = MIN_INTERVAL
    MINUTES_TO_SECONDS = 60

    PARSER = argparse.ArgumentParser(description='Get value of stock with regular interval')
    PARSER.add_argument("company_symbol",
                        help="Specify the symbol name of company")
    PARSER.add_argument("-i", "--interval", type=check_negative,
                        help="Interval for regular checking in minutes. Default values is {}. "
                             "Minimum value is {}".format(DEF_INTERVAL, MIN_INTERVAL))

    ARGS = PARSER.parse_args()

    COMPANY_SYMBOL = ARGS.company_symbol

    if ARGS.interval:
        INTERVAL = int(ARGS.interval)
    else:
        INTERVAL = DEF_INTERVAL

    if INTERVAL < MIN_INTERVAL:
        INTERVAL = MIN_INTERVAL

    print("")
    print("Getting stock of {} with regular interval {} minutes".format(COMPANY_SYMBOL, INTERVAL))
    print("")

    LAST_STOCK_VALUE = 0
    FIRST_TIME = True

    while True:
        CURR_STOCK_VALUE = get_stock_value(COMPANY_SYMBOL)

        if CURR_STOCK_VALUE is None:
            print("error Happening...")
            print("program Quitting")
            break
        else:
            if CURR_STOCK_VALUE[1] < LAST_STOCK_VALUE:
                STATUS = "[DOWN]"
            elif CURR_STOCK_VALUE[1] > LAST_STOCK_VALUE:
                STATUS = "[UP]"
            else:
                STATUS = "[EQUAL]"

            NOW_STR = time.strftime('%Y-%m-%d %H:%M')

            if FIRST_TIME:
                STATUS = ""
                FIRST_TIME = False

            print("{} | {} | {}".format(NOW_STR, CURR_STOCK_VALUE[1], STATUS))

            LAST_STOCK_VALUE = CURR_STOCK_VALUE[1]

        time.sleep(INTERVAL * MINUTES_TO_SECONDS)
