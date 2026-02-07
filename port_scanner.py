import socket

target = input("Enter target IP or website: ").strip()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid host or network issue.")
    exit()

print("\nScanning target:", target_ip)
print("Please wait...\n")

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB"
}

for port in range(20, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        service = common_ports.get(port, "Unknown Service")
        print(f"Port {port} OPEN ({service})")

    s.close()

print("\nScan complete.")
