# PcapPoisoning - Forensics Challenge Writeup

## Challenge Description
How about some hide and seek heh? Download this file and find the flag.

## Solution

This challenge provides a packet capture file (`trace.pcap`) that we need to analyze to find the hidden flag.

### Method 1: Manual Investigation with Wireshark

I started by opening the packet capture file in Wireshark and manually browsing through the packets in chronological order:

1. After analyzing several hundred packets, I found the flag in packet #507
2. This packet uses the TCP protocol and contains the flag in plaintext
3. The hex dump of the packet clearly shows the flag:

```
0000   45 00 00 52 00 01 00 00 40 06 c3 90 ac 10 00 02   E..R....@.......
0010   0a fd 00 06 00 14 00 15 00 00 00 00 00 00 00 00   ................
0020   50 02 20 00 8b 73 00 00 70 69 63 6f 43 54 46 7b   P. ..s..picoCTF{
0030   50 36 34 50 5f 34 4e 34 4c 37 53 31 53 5f 53 55   P64P_4N4L7S1S_SU
0040   35 35 33 35 35 46 55 4c 5f 35 62 36 61 36 30 36   55355FUL_5b6a606
0050   31 7d                                             1}
```

### Method 2: Quick String Extraction

Alternatively, we can extract all strings from the pcap file and grep for the flag format:

```bash
strings trace.pcap | grep pico
```

This outputs the flag directly:
```
picoCTF{P64P_4N4L7S1S_SU55355FUL_5b6a6061}
```

## Flag
`picoCTF{P64P_4N4L7S1S_SU55355FUL_5b6a6061}`

## Tools Used
- Wireshark
- Basic command-line utilities (strings, grep)

## Learning Points
- PCAP files contain raw packet data that can include plaintext information
- Sometimes simple approaches like string extraction can quickly solve forensics challenges
- Manual packet inspection provides deeper understanding of the challenge
