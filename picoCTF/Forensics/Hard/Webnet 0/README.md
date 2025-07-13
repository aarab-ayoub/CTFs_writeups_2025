# Webnet 0 - PicoCTF Challenge Writeup

## Challenge Information
- **Name**: Webnet 0
- **Category**: Forensics / Network Analysis
- **Difficulty**: Hard
- **Description**: We found this packet capture and key. Recover the flag.
- **Files**: 
  - Packet capture file (.pcap/.pcapng)
  - TLS private key file
- **Hints**:
  1. Try using a tool like Wireshark.
  2. How can you decrypt the TLS stream?

## Solution Overview

This challenge involves analyzing encrypted TLS traffic and using a provided private key to decrypt the communication and extract the flag. The solution demonstrates TLS decryption techniques and network traffic analysis.

## Step-by-Step Solution

### Step 1: Understanding the Challenge
We have two files:
- A packet capture containing encrypted TLS/HTTPS traffic
- A private key file that can decrypt this traffic

The goal is to use the private key to decrypt the TLS streams and find the flag hidden in the HTTP communication.

### Step 2: Open the Packet Capture in Wireshark
Load the packet capture file in Wireshark:

```bash
wireshark [capture_file].pcap
```

Initially, you'll see encrypted TLS traffic that appears as unintelligible encrypted data.

### Step 3: Configure TLS Decryption in Wireshark

#### Understanding the Key File
The provided key file is a **TLS/SSL private key**, specifically:
- **Type**: RSA private key in PEM format
- **Purpose**: Server's private key corresponding to its certificate
- **Function**: Allows decryption of TLS traffic encrypted with RSA key exchange

#### Configure Wireshark for TLS Decryption
1. Go to **Edit** → **Preferences**
2. Navigate to **Protocols** → **TLS** (or **SSL** in older versions)
3. Click on **RSA keys list** → **Edit**
4. Add a new entry with:
   - **IP Address**: Server's IP address from the capture
   - **Port**: 443 (standard HTTPS port)
   - **Protocol**: http
   - **Key File**: Browse and select the provided private key file

### Step 4: Apply the Configuration
After adding the RSA key:
1. Click **OK** to save the configuration
2. Reload the capture or restart Wireshark
3. The encrypted TLS streams should now appear as decrypted HTTP traffic

### Step 5: Analyze the Decrypted Traffic
With the TLS decryption enabled, you can now:
- Follow HTTP streams instead of encrypted TLS streams
- View the actual HTTP requests and responses
- Search for flags in the decrypted content

### Step 6: Locate the Flag
Browse through the decrypted HTTP streams to find the flag. In this case, the flag was found in an HTTP response header:

```http
HTTP/1.1 200 OK
Date: Fri, 23 Aug 2019 15:56:36 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Mon, 12 Aug 2019 16:50:05 GMT
ETag: "5ff-58fee50dc3fb0-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Encoding: gzip
Pico-Flag: picoCTF{nongshim.shrimp.crackers}
Content-Length: 821
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html
```

The flag is embedded in a custom HTTP header: `Pico-Flag: picoCTF{nongshim.shrimp.crackers}`

## Key Concepts Learned

### TLS/SSL Decryption
1. **RSA Key Exchange**: Uses server's private key to decrypt pre-master secret
2. **Session Keys**: Derived from pre-master secret to encrypt/decrypt actual data
3. **Forward Secrecy**: Modern TLS with ECDHE/DHE prevents this type of decryption

### Network Forensics
1. **Packet Analysis**: Understanding network protocols and traffic flow
2. **Protocol Layers**: TLS encryption wraps HTTP communication
3. **Traffic Decryption**: Using cryptographic keys to reveal encrypted content

### Wireshark Usage
1. **Protocol Configuration**: Setting up decryption parameters
2. **Stream Following**: Analyzing complete conversations
3. **Filter Usage**: Focusing on specific types of traffic

## Tools Used
- **Wireshark** - Network protocol analyzer and packet capture tool
- **TLS Private Key** - For decrypting encrypted traffic

## TLS Decryption Requirements

### What You Need:
1. **Server's Private Key**: The private key corresponding to the server's certificate
2. **RSA Key Exchange**: The TLS connection must use RSA key exchange (not ECDHE/DHE)
3. **Complete Handshake**: The packet capture must include the full TLS handshake

### Limitations:
- **Forward Secrecy**: Connections using ECDHE/DHE key exchange cannot be decrypted this way
- **Key Availability**: Server private keys are typically not available to attackers
- **Modern TLS**: Current TLS implementations prefer forward secrecy methods

## File Format Reference

### RSA Private Key Format (PEM):
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA...
[Base64 encoded key data]
...
-----END RSA PRIVATE KEY-----
```

### Alternative Formats:
- **PKCS#8**: `-----BEGIN PRIVATE KEY-----`
- **PKCS#1**: `-----BEGIN RSA PRIVATE KEY-----`
- **DER**: Binary format (less common for CTF challenges)

## Security Implications

1. **Key Compromise**: If a server's private key is compromised, all past traffic can be decrypted
2. **Forward Secrecy**: Modern systems use ephemeral key exchange to prevent this
3. **Key Management**: Proper key rotation and protection are crucial
4. **Traffic Analysis**: Encrypted traffic can still reveal metadata and patterns

## Alternative Analysis Methods

1. **Command Line Tools**:
   ```bash
   # Using tshark for automated analysis
   tshark -r capture.pcap -o tls.keylog_file:keyfile.key
   ```

2. **SSL/TLS Key Log Files**: Modern browsers can export key logs for debugging
3. **Custom Scripts**: Python with scapy for programmatic analysis

## Flag
```
picoCTF{nongshim.shrimp.crackers}
```

## Conclusion

This challenge demonstrates the importance of proper TLS implementation and key management. While the ability to decrypt TLS traffic with a private key is a powerful forensic technique, it also highlights why forward secrecy is crucial in modern cryptographic implementations. The challenge shows how network traffic analysis combined with cryptographic knowledge can reveal hidden information in seemingly secure communications.

The flag's location in a custom HTTP header (`Pico-Flag`) is a nice touch that requires careful examination of the decrypted traffic, not just automated flag detection tools.
