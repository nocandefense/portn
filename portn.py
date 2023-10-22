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
	1723: ("PPTP", "TCP"),
    1701: ("L2TP", "UDP"),
    500: ("IPsec/L2TP", "UDP"),
    4500: ("IPsec NAT-Traversal", "UDP"),
    443: ("SSTP/HTTPS", "TCP"),  # Note: 443 is also used for HTTPS, so this entry might override it
    1194: ("OpenVPN", "Both")
}

def lookup_by_port(port):
    return services.get(port, ("Unknown", "Unknown"))

def lookup_by_protocol_name(protocol_name):
    results = [(port, name) for port, (name, protocol) in services.items() if name.lower() == protocol_name.lower()]
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:")
        print("Lookup by port: script_name <port_number>")
        print("Lookup by protocol name: script_name <protocol_name>")
        sys.exit(1)

    arg = sys.argv[1]
    if arg.isdigit():
        port = int(arg)
        service, protocol = lookup_by_port(port)
        print(f"Port {port} is commonly used for {service} over {protocol}")
    else:
        protocol_name = arg
        results = lookup_by_protocol_name(protocol_name)
        if results:
            for port, name in results:
                print(f"{name} commonly runs on port {port}")
        else:
            print(f"No results found for protocol name: {protocol_name}")

