"""
Whois Search Tool - Enter an IP or host address and have it look it up through whois and return
the results to you.
"""
from subprocess import call

if __name__ == '__main__':
    IP = input("Enter an IP : ")
    print(call(["whois", IP]))
