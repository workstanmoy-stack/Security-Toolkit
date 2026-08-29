import socket


def scan_ports(target, ports):

    results = []

    try:
        ip = socket.gethostbyname(target)

    except socket.gaierror:
        return [("ERROR", "Could not resolve hostname.")]

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(0.5)

        try:
            result = sock.connect_ex((ip, port))

            if result == 0:
                status = "OPEN"

            else:
                status = "CLOSED"

        except socket.error:
            status = "ERROR"

        finally:
            sock.close()

        results.append((port, status))

    return results


import socket


def scan_ports(target, ports):

    results = []

    try:
        ip = socket.gethostbyname(target)

    except socket.gaierror:
        return [("ERROR", "Could not resolve hostname.")]

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(0.5)

        try:
            result = sock.connect_ex((ip, port))

            if result == 0:
                status = "OPEN"
            else:
                status = "CLOSED"

        except socket.error:
            status = "ERROR"

        finally:
            sock.close()

        results.append((port, status))

    return results
