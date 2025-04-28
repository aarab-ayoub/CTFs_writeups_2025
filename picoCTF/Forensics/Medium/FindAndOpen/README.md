# FindAndOpen Writeup

## Challenge Information
- **Name**: FindAndOpen
- **Description**: Someone might have hidden the password in the trace file. Find the key to unlock this file. This tracefile might be good to analyze.
- **Hints**: 
  - Download the pcap and look for the password or flag.
  - Don't try to use a password cracking tool, there are easier ways here.

## Understanding the Challenge

For this challenge, we're provided with a network packet capture (PCAP) file. The description hints that there's a hidden password within the trace file that can be used to unlock another file (presumably the flag file, which appears to be a ZIP archive).

## Analysis Process

### Step 1: Examining the PCAP with Wireshark

Opening the provided PCAP file with Wireshark reveals a variety of network traffic. After some initial inspection, we notice:

- Many MDNS (Multicast DNS) protocol packets that don't contain any meaningful data
- Several packets with "Ethernet II" in the info column

### Step 2: Looking for Anomalies

While examining the Ethernet II packets, I noticed that most packets had lengths of 43, 46, 47, or 49 bytes. However, one packet stood out with a length of 70 bytes.

This anomaly is worth investigating further, as unusual packet sizes often indicate hidden information in network forensics challenges.

### Step 3: Extracting the Hidden Data

Upon examining the content of the 70-byte packet, I found a Base64-encoded string:

```
VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
```

### Step 4: Decoding the Base64 String

Decoding this Base64 string reveals:

```
This is the secret: picoCTF{R34DING_LOKd_
```

The string appears to be a partial flag or password. The incomplete nature of the decoded text suggests that it's meant to be used as a password for unlocking the provided ZIP file.

### Step 5: Unlocking the ZIP File

Using the discovered password (`picoCTF{R34DING_LOKd_`) to extract the contents of the flag.zip file:

```bash
unzip -P "picoCTF{R34DING_LOKd_" flag.zip
```

### Step 6: Retrieving the Flag

After successfully extracting the ZIP file, I was able to read the flag:

```bash
cat flag
picoCTF{R34DING_LOKd_fil56_succ3ss_5ed3a878}
```

## The Flag

The complete flag is:
```
picoCTF{R34DING_LOKd_fil56_succ3ss_5ed3a878}
```

## Reflection

This challenge illustrates the importance of:

1. **Identifying anomalies in network traffic** - The unusually sized packet was the key to finding the hidden data
2. **Understanding common encoding techniques** - Recognizing and decoding Base64 content
3. **Paying attention to file formats** - Using the partial flag as a password for the ZIP file

The challenge name "FindAndOpen" was quite literal - we needed to find the password in the trace file and use it to open the encrypted archive. The hint about not needing password cracking tools was accurate, as the password was hidden in plain sight within the network capture.

This type of challenge is common in forensics categories of CTF competitions, where data is often hidden within seemingly normal network traffic or files.
