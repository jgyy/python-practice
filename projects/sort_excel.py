"""
Sort Excel/CSV File Utility - Reads a file of records, sorts them, and then writes them back to
the file. Allow the user to choose various sort style and sorting based on a particular field.
"""
import pandas as pd

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)

    # Source Info
    FILE = input('Enter location/name of file ')
    SHEET = input('Enter sheet name you wish to sort ')
    FILE_2 = pd.read_excel(FILE, SHEET, index_col=0, na_values=['NA'])

    # Sort Info
    SORTER = []
    STYLE = []
    SORT_Q = int(input("Please enter # of  column you wish to sort by: "))
    for x in range(SORT_Q):
        SORTER.append(input(('Name of columns you wish to sort by ' + repr(x + 1) + ' ')))
        STYLE.append(input(('Type True for Ascending, False for Descending sort ' +
                            repr(x + 1) + ' ')))
    SORT_1 = FILE_2.sort(SORTER, ascending=STYLE)

    # Destination Info
    DEST_WB = input('Enter destination and filename you wish to store as ')
    SORT_1.to_excel(DEST_WB, sheet_name='Sheet1')
