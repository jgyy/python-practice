"""
Port Scanner - Enter an IP address and a port range where the program will then attempt to find
open ports on the given computer by connecting to each of them. On any successful connections
mark the port as open.
"""
import socket
import sys

if __name__ == '__main__':
    def connect_to_ip(connect_ip, connect_port):
        """
        :param connect_ip:
        :param connect_port:
        :return:
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((connect_ip, connect_port))
            return sock
        except TypeError:
            return None


    def scan_port(scan_ip, scan_main_port, scan_timeout):
        """
        :param scan_ip:
        :param scan_main_port:
        :param scan_timeout:
        """
        socket.setdefaulttimeout(scan_timeout)
        sock = connect_to_ip(scan_ip, scan_main_port)

        if sock:
            print('Able to connect to: {0}:{1}'.format(scan_ip, scan_main_port))
            sock.close()
        else:
            print('Not able to connect to: {0}:{1}'.format(scan_ip, scan_main_port))


    # Get the IP / domain from the user
    IP_DOMAIN = input("Enter the ip or domain: ")
    if IP_DOMAIN == '':
        print('You must specify a host!')
        sys.exit(0)

    # Get the port range from the user
    PORT = input("Enter the port range (Ex 20-80): ")
    if PORT == '':
        print('You must specify a port range!')
        sys.exit(0)

    # Optional: Get the timeout from the user
    TIMEOUT = input("Timeout (Default=5): ")
    if not TIMEOUT:
        TIMEOUT = 5

    PORT_RANGE = PORT.split("-")

    # Get the IP address if the host name is a domain
    try:
        IP = socket.gethostbyname(IP_DOMAIN)
    except TypeError:
        print('There was an error resolving the domain')
        sys.exit(1)

    # If the user only entered one port we will only scan the one port
    # otherwise scan the range
    if len(PORT_RANGE) < 2:
        scan_port(IP, int(PORT), int(TIMEOUT))
    else:
        for PORT in range(int(PORT_RANGE[0]), int(PORT_RANGE[1]) + 1):
            scan_port(IP, int(PORT), int(TIMEOUT))
