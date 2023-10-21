#!/usr/bin/env python3

import sys

# Define a dictionary of common services and their ports
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    443: "HTTPS",
    445: "Microsoft-DS",
    993: "IMAP over SSL",
    995: "POP3 over SSL",
    3306: "MySQL",
    3389: "MS RDP",
    5900: "VNC",
    # ... Add more as needed
}

def get_service(port):
    return services.get(port, "Unknown")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script_name <port_number>")
        sys.exit(1)

    port = int(sys.argv[1])
    service = get_service(port)
    print(f"Port {port} is commonly used for {service}")

