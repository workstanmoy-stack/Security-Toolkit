import socket


def lookup_ip(hostname):

    try:
        ip = socket.gethostbyname(hostname)

        return ip

    except socket.gaierror:
        return None
