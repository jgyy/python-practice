"""
Remote SQL Tool - A utility that can execute queries on remote servers from your local computer
across the Internet. It should take in a remote host, user name and password, run the query and
return the results.
"""
import pymysql
from prettytable import from_db_cursor

if __name__ == '__main__':
    HOST = input('Enter host name ')
    USER = input('Enter username ')
    PASSWORD = input('Enter password ')
    DATABASE = input('Enter DB ')
    DB = pymysql.connect(HOST,  # your host, usually localhost
                         USER,  # your username
                         PASSWORD,  # your password
                         DATABASE)  # name of the data base

    # Create a Cursor object
    CUR = DB.cursor()
    COL = input('Enter Column Name')
    TABLE = input('Enter Table name')
    # columns = map(col, col.split())
    CUR.execute("SELECT " + COL + " FROM " + DATABASE + "." + TABLE + "")
    PT = from_db_cursor(CUR)
    print(PT)
    CUR.close()
