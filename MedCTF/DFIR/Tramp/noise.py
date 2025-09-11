# Save as noise.py
from scapy.all import *
from random import randint

# Generate 1000 fake HTTP/TCP packets to obscure the real traffic
for _ in range(1000):
    fake_ip = "192.168." + ".".join(map(str, [randint(1,254) for _ in range(2)]))
    send(IP(src=fake_ip, dst="10.0.0.1")/TCP()/Raw(load="Noise data"))