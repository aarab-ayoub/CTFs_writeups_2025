# 🚩 DRIF CTF Challenge: Covert Data Exfiltration

## 📝 Challenge Overview

This CTF challenge demonstrates advanced data exfiltration techniques using DNS and ICMP protocols, showcasing how attackers can stealthily transmit information across networks.

## 🔍 Challenge Components

### 1. Data Exfiltration Techniques
- **DNS Exfiltration**: Hiding data in DNS query subdomains
- **ICMP Exfiltration**: Embedding payload in ICMP packet payloads
- **Noise Generation**: Creating background network traffic to mask exfiltration

### 2. Key Techniques Used
- Base64 Encoding
- XOR Encryption
- Hex Manipulation
- Protocol Abuse

## 🛠️ Challenge Scripts

### `dns_exfil.py`
```python
# DNS Exfiltration Method
def exfiltrate_via_dns(flag_part):
    # 1. XOR Encryption with 'deadbeef' key
    # 2. Base64 Encoding
    # 3. Split into DNS subdomain queries
    # 4. Send queries to 8.8.8.8
```

### `icmp_exfil.py`
```python
# ICMP Exfiltration Method
def exfiltrate_via_icmp(flag_part):
    # 1. Base64 Encoding
    # 2. Hex Conversion
    # 3. Reverse Hex String
    # 4. Send in ICMP packet payloads to 1.1.1.1
```

### `noise.py`
```python
# Network Noise Generation
def generate_noise():
    # Create 1000 fake HTTP/TCP packets
    # Randomize source IPs
    # Obscure real exfiltration traffic
```

## 🕵️ Exfiltration Breakdown

### DNS Exfiltration Process
1. XOR encrypt flag part with `deadbeef` key
2. Base64 encode the result
3. Split encoded data into 3-character subdomains
4. Send DNS queries to `8.8.8.8`
   - Example: `abc.evil-domain.lol`

### ICMP Exfiltration Process
1. Base64 encode flag part
2. Convert to hex
3. Reverse hex string
4. Split into 16-character chunks
5. Send via ICMP packets to `1.1.1.1`

## 🔓 Solution Script Walkthrough

### Key Decoding Steps
- Extract DNS subdomain queries
- Reconstruct Base64 payload
- XOR decrypt with `deadbeef` key
- Extract ICMP hex payloads
- Reverse and decode

## 💡 Learning Objectives

- Network protocol abuse
- Stealth data transmission techniques
- Encryption and encoding methods
- Network forensics
- Packet analysis

## 🛡️ Mitigation Strategies

1. **DNS Filtering**
   - Implement strict DNS query monitoring
   - Use DNS filtering solutions
   - Block unknown or suspicious domains

2. **ICMP Traffic Control**
   - Limit ICMP traffic
   - Implement ICMP filtering
   - Monitor unusual ICMP patterns

3. **Network Monitoring**
   - Use advanced network detection systems
   - Implement packet inspection
   - Monitor for unusual encoding/transmission patterns

## 🧰 Required Tools

- Python 3.x
- Scapy
- Wireshark/tcpdump
- Base64 library
- Argparse

## 🚀 Running the Challenge

### Prerequisites
```bash
pip install scapy
```

### Solution Execution
```bash
python solve_challenge.py captured_network_traffic.pcapng
```

## ⚠️ Disclaimer

> **Warning**: This challenge is for educational purposes only. Always obtain proper authorization before performing network security testing.

## 📚 Further Reading
- [SANS Institute: DNS Tunneling](https://www.sans.org/blog/dns-tunneling/)
- [OWASP: Data Exfiltration](https://owasp.org/www-community/attacks/Data_Exfiltration)
- [Network Protocol Abuse Techniques](https://attack.mitre.org/techniques/T1048/)

## 🤝 Contributions
Improvements and insights are welcome! Open an issue or submit a pull request.

---

*Happy Hacking! 🌐🔐*