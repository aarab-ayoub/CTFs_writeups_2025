# Ph4nt0m 1ntrud3r - Forensics Challenge Writeup

## Challenge Description
A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag. To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!

## Solution

This challenge involves analyzing network traffic in a PCAP file to identify how an attacker infiltrated a system and to recover the hidden flag.

### Step 1: Initial Analysis with Wireshark

I began by opening the provided PCAP file (`myNetworkTraffic.pcap`) using Wireshark. Initial observation showed primarily TCP packets, each containing data encoded in base64. An important discovery was that the packets were not chronologically ordered by capture time, which would become significant later.

### Step 2: Extracting TCP Data

My first approach was to use tshark (the command-line version of Wireshark) to extract all TCP data:

```bash
tshark -r myNetworkTraffic.pcap -Y "tcp" -T fields -e tcp.segment_data | xxd -p -r | base64 -d
```

This command:
- Reads the PCAP file
- Filters for TCP packets
- Extracts the segment data
- Converts from hex to binary
- Decodes from base64

However, this approach didn't yield the correct flag because it included unnecessary packets.

### Step 3: Refining the Packet Filter

After analyzing the packet sizes, I noticed that the relevant data appeared to be in TCP packets with a length of 12 bytes. I refined my command:

```bash
tshark -r myNetworkTraffic.pcap -Y "tcp.len==12" -T fields -e tcp.segment_data | xxd -p -r | base64 -d
```

This produced parts of the flag, but they were still not in the correct order due to the non-chronological capture times.

### Step 4: Sorting by Capture Time

Finally, I created a command that would:
1. Filter for TCP packets with length 12 or 4 bytes
2. Extract both the capture time and the data
3. Sort the packets by capture time
4. Extract only the data field
5. Convert from hex and decode from base64

```bash
tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data | sort -k4 | awk '{print $6}' | xxd -p -r | base64 -d
```

Command breakdown:
- `tshark -r myNetworkTraffic.pcap`: Read the PCAP file
- `-Y "tcp.len==12 || tcp.len==4"`: Filter TCP packets with length 12 or 4 bytes
- `-T fields -e frame.time -e tcp.segment_data`: Extract timestamp and data fields
- `sort -k4`: Sort based on the 4th field (timestamp)
- `awk '{print $6}'`: Print only the 6th field (data)
- `xxd -p -r`: Convert hex dump to binary
- `base64 -d`: Decode from base64

This approach successfully recovered the complete flag in the correct order.

## Flag
*Note: The actual flag value was not provided in the challenge description*

## Tools Used
- Wireshark (GUI network analyzer)
- tshark (command-line network analyzer)
- xxd (hex dump utility)
- base64 (encoding/decoding utility)
- sort and awk (text processing utilities)

## Learning Points
- Network packets may not always be in chronological order in PCAP files
- Base64 encoding is commonly used to transmit binary data in text form
- Packet length can be a useful filter criterion when looking for specific data
- Command-line tools can be combined effectively for forensic analysis
- Timestamp information is crucial for reconstructing the correct sequence of events
