"""
Binary to Decimal and Back Converter - Develop a converter to convert a decimal number
to binary or a binary number to its decimal equivalent.
"""
import urllib.request
import json


class Converter:
    """Binary to Decimal and Back Converter"""
    _temps = {'cf': lambda c: c * (9 / 5) + 32,
              'fc': lambda f: (f - 32) * (5 / 9),
              'ck': lambda c: c + 273.15,
              'kc': lambda k: k - 273.15,
              'fk': lambda f: (f + 459.67) * 5 / 9,
              'kf': lambda k: k * (9 / 5) - 459.67
              }

    @classmethod
    def bin_to_dec(cls, bin_no):
        """
        @param bin_no:  an integer or str representation of a binary number
        @return:        an integer value of the binary number passed
        """
        dec = 0
        i = 0
        if not isinstance(bin_no, int):
            try:
                bin_no = int(bin_no)
            except TypeError:
                raise TypeError
        while bin_no > 0:
            dec += ((bin_no % 10) * (2 ** i))
            bin_no //= 10
            i += 1
        return dec

    @classmethod
    def dec_to_bin(cls, dec_no, bit_rep):
        """
        @param dec_no:  an integer value
        @param bit_rep: bit representation amount
        @return:        a string representation of the decimal value passed
        """
        dec_no = int(dec_no)
        if dec_no > 0:
            return str(bin(dec_no)[2:].zfill(bit_rep))
        return '-' + str(bin(dec_no))[2:].zfill(bit_rep)

    @classmethod
    def currency_exchange(cls, con_from, con_to, value):
        """
        @param con_from:a string representation of the currency to convert from
        @param con_to:  a string representation of the currency to convert to
        @param value:   amount to convert
        @return:        the value of the conversion from con_from to con_to of value
        """
        curr_page = urllib.request.urlopen(
            'http://openexchangerates.org/api/latest.json?app_id=9f0710764c064370932f4f2496968c62')
        obj = curr_page.read().decode(encoding='UTF-8')
        content = json.loads(obj)
        value = int(value)
        try:
            _from = content['rates'][con_from.upper()]
            _to = content['rates'][con_to.upper()]
            convert_amt = _to / _from
            result = convert_amt * value
        except NameError:
            raise NameError
        return result

    @classmethod
    def temp_convert(cls, msr_from, msr_to, amt):
        """
        Rounding off the final value to 2 digit
        @param msr_from:a string representation of the measurement to convert from
        @param msr_to:  a string representation of the measurement to convert to
        @param amt:     the value to convert
        @return:        the converted temperature value
        """
        try:
            result = cls._temps[(msr_from[0] + msr_to[0]).lower()](int(amt))
            return round(result, 2)
        except KeyError:
            "Cannot convert from {0} to {1}".format(msr_from, msr_to)


if __name__ == "__main__":
    print("Binary to Decimal and Back Converter - Develop a converter to convert "
          "a decimal number to binary or a binary number to its decimal equivalent.")
    BIN_INPUT = input("Enter binary number here: ")
    BIN = Converter.bin_to_dec(BIN_INPUT)
    print("Decimal number is " + str(BIN))
    DEC_INPUT = input("Enter decimal number here: ")
    DEC = Converter.dec_to_bin(DEC_INPUT, 32)
    print("Binary number is " + DEC)
    print("Currency code list: AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, "
          "BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTC, BTN, BWP, BYN, BZD, CAD, CDF, "
          "CHF, CLF, CLP, CNH, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, "
          "ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, "
          "HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, "
          "KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, "
          "MKD, MMK, MNT, MOP, MRO, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, "
          "NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, "
          "SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STD, STN, SVC, SYP, SZL, THB, "
          "TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, UYU, UZS, VEF, VES, VND, "
          "VUV, WST, XAF, XAG, XAU, XCD, XDR, XOF, XPD, XPF, XPT, YER, ZAR, ZMW, ZWL \n")
    CON_FROM = input("Enter currency code from: ")
    CON_TO = input("Enter currency code to: ")
    AMOUNT = input("Enter the amount in " + CON_FROM + ": ")
    CON = Converter.currency_exchange(CON_FROM, CON_TO, AMOUNT)
    print("Value in " + CON_TO + " is: " + str(CON))
    TEMP_FROM = input("Enter temperature unit to convert from: ")
    TEMP_TO = input("Enter temperature unit to convert to: ")
    TEMP_VALUE = input("Enter temperature value in " + TEMP_FROM[0] + ": ")
    TEMP = Converter.temp_convert(TEMP_FROM, TEMP_TO, TEMP_VALUE)
    print("The temperature in " + TEMP_TO[0] + " is " + str(TEMP))
