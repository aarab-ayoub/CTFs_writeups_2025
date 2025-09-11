from scapy.all import rdpcap, DNSQR, ICMP, Raw, IP
import base64
import argparse

def decode_dns_part(packets):
    """Extract and decode DNS exfiltrated payload"""
    subdomains = []
    for pkt in packets:
        # Filter only relevant DNS queries
        if (pkt.haslayer(DNSQR) 
            and pkt.haslayer(IP) 
            and pkt[IP].dst == "8.8.8.8"
            and "evil-domain.lol" in str(pkt[DNSQR].qname)):
            
            # Extract subdomain prefix
            subdomain = pkt[DNSQR].qname.decode().split('.')[0]
            subdomains.append(subdomain)
    
    # Remove duplicates while preserving order
    subdomains = list(dict.fromkeys(subdomains))
    b64_str = ''.join(subdomains)
    
    # Add Base64 padding if needed
    padding = '=' * (-len(b64_str) % 4)
    xor_encoded_bytes = base64.b64decode(b64_str + padding)
    
    # Convert to Unicode string (original XOR was done on code points)
    encoded_str = xor_encoded_bytes.decode('utf-8')
    
    # XOR decrypt with deadbeef key
    xor_key = bytes.fromhex("deadbeef")
    decoded_chars = []
    for i, c in enumerate(encoded_str):
        key_byte = xor_key[i % 4]  # Cycle through 4-byte key
        decoded_chars.append(chr(ord(c) ^ key_byte))
    
    return ''.join(decoded_chars)

def decode_icmp_part(packets):
    """Extract and decode ICMP exfiltrated payload"""
    hex_payloads = []
    for pkt in packets:
        if (pkt.haslayer(ICMP) 
            and pkt.haslayer(Raw) 
            and pkt.haslayer(IP) 
            and pkt[IP].dst == "1.1.1.1"):
            
            # Extract ASCII hex string from payload
            hex_payloads.append(pkt[Raw].load.decode('utf-8'))
            print(f"Extracted hex payload: {pkt[Raw].load.decode('utf-8')}")
    
    # Reconstruct and decode
    full_hex = ''.join(hex_payloads)
    print(f"Full hex string: {full_hex}")
    reversed_hex = full_hex[::-1]
    print(f"Reversed hex string: {reversed_hex}")
    return base64.b64decode(bytes.fromhex(reversed_hex)).decode()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve CTF challenge')
    parser.add_argument('pcap_file', help='Path to PCAPNG file')
    args = parser.parse_args()

    try:
        packets = rdpcap(args.pcap_file)
        dns_part = decode_dns_part(packets)
        icmp_part = decode_icmp_part(packets)
        print(f"Flag: {dns_part}{icmp_part}")
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Common issues:\n"
              "1. PCAP file not found\n"
              "2. Missing Scapy (pip install scapy)\n"
              "3. Network packets out of order")