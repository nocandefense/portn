#!/usr/bin/env python3

import sys

# Define a dictionary of common services, their ports, and protocols
services = {
    20: ("FTP Data", "TCP"),
    21: ("FTP Control", "TCP"),
    22: ("SSH", "TCP"),
    23: ("Telnet", "TCP"),
    25: ("SMTP", "TCP"),
    53: ("DNS", "Both"),
    67: ("DHCP Server", "UDP"),
    68: ("DHCP Client", "UDP"),
    69: ("TFTP", "UDP"),
    80: ("HTTP", "TCP"),
    110: ("POP3", "TCP"),
    119: ("NNTP", "TCP"),
    123: ("NTP", "UDP"),
    135: ("MS RPC", "TCP"),
    137: ("NetBIOS Name Service", "UDP"),
    138: ("NetBIOS Datagram Service", "UDP"),
    139: ("NetBIOS Session Service", "TCP"),
    143: ("IMAP", "TCP"),
    161: ("SNMP", "UDP"),
    162: ("SNMP Trap", "UDP"),
    389: ("LDAP", "TCP"),
    443: ("HTTPS", "TCP"),
    445: ("Microsoft-DS", "TCP"),
    500: ("ISAKMP", "UDP"),
    636: ("LDAPS", "TCP"),
    989: ("FTPS Data", "TCP"),
    990: ("FTPS Control", "TCP"),
    993: ("IMAP over SSL", "TCP"),
    995: ("POP3 over SSL", "TCP"),
    1812: ("RADIUS Authentication", "UDP"),
    1813: ("RADIUS Accounting", "UDP"),
    3389: ("MS RDP", "TCP"),
    5060: ("SIP", "UDP"),
    5061: ("SIPS", "TCP"),
    5900: ("VNC", "TCP"),
    # ... Add more as needed
}

def get_service(port):
    return services.get(port, ("Unknown", "Unknown"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script_name <port_number>")
        sys.exit(1)

    port = int(sys.argv[1])
    service, protocol = get_service(port)
    print(f"Port {port} is commonly used for {service} over {protocol}")

