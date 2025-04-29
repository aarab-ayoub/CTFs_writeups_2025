# CTF Challenge: Packets Primer

## Challenge Description
Download the packet capture file and use packet analysis software to find the flag.
* Download packet capture

**Hint:** Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.

## Solution Approach

### Method 1: Using Wireshark

Wireshark is a powerful network protocol analyzer that allows us to inspect packet data in network capture files.

1. Downloaded the provided PCAP file (`network-dump.flag.pcap`)
2. Opened the file in Wireshark
3. Examined the packets in the capture
4. Looking through the TCP protocol packets, the flag was visible in packet #4


The flag was clearly visible in the packet data:
```
picoCTF{p4ck37_5h4rk_ceccaa7f}
```

### Method 2: Using strings command

An even simpler approach is to use the `strings` command to extract all readable text from the binary PCAP file:

```bash
strings network-dump.flag.pcap
```

Output:
```
k&Nar
n#('
k&Na
k&Na`
n#('
k&Na;
n#('
p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ c e c c a a 7 f }
k&Naa
ep&Na(
p&NaX
p&Na28
p&Na
```

The flag is clearly visible in the output with spaces between each character.

## Tools Used
- **Wireshark** - Network protocol analyzer for examining packet data
- **strings** - Unix utility for finding printable strings in binary files

## Conclusion
This challenge demonstrates basic packet analysis techniques. While Wireshark provides a comprehensive view of network traffic, sometimes simple command-line tools like `strings` can quickly reveal the information we're looking for, especially when flag data is stored as plain text within packets.

## Flag
`picoCTF{p4ck37_5h4rk_ceccaa7f}`
