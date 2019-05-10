"""
Tax Calculator - Asks the user to enter a cost and either a country or state tax.
It then returns the tax plus the total cost with tax.
"""
TAX_RATES = {
    'State': {
        'AZ': .056,
        'CO': .029,
        'MT': 0.0,
        'NV': .0685,
        'TX': .0625
    },
    'Country': {
        'CAN': .05,
        'UK': .2,
        'ESP': .21,
        'GER': .19,
        'JAP': .08
    }
}
if __name__ == "__main__":
    print("Enter tax lookup \n \
    1: Country \n \
    2: State\n")

    TAX_LOOKUP = int(input())
    if TAX_LOOKUP == 1:
        CHOICE = 'Country'
    else:
        CHOICE = 'State'

    COST = float(input("Enter Cost: "))
    RATE = str(input("Select Tax Rate (%s): " %
                     ','.join(TAX_RATES[CHOICE].keys()))).upper()
    print("Cost of %.2f in %s is %.2f" %
          (COST, RATE, float(COST + (COST * TAX_RATES[CHOICE][RATE]))))
