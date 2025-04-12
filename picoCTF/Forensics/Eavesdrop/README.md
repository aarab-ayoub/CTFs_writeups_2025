# CTF Forensics Challenge: Chat and File Transfer

## Challenge Overview
In this forensics challenge, we were provided with a packet capture (.pcap) file. The challenge description stated: "All we know is that this packet capture includes a chat conversation and a file transfer."

## Initial Analysis
Opening the .pcap file in a packet analysis tool (like Wireshark), I began by examining the TCP streams to find any readable conversations.

## Finding the Chat Conversation
Following the TCP streams, I discovered a chat conversation between two individuals discussing how to decrypt a file:

```
Person 1: Hey, how do you decrypt this file again?
Person 2: You're serious?
Person 1: Yeah, I'm serious
Person 2: *sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
Person 1: Ok, great, thanks.
Person 1: Let's use Discord next time, it's more secure.
Person 2: C'mon, no one knows we use this program like this!
Person 1: Whatever.
Person 2: Hey.
Person 1: Yeah?
Person 2: Could you transfer the file to me again?
Person 1: Oh great.
Person 1: Ok, over 9002?
Person 2: Yeah, listening.
Person 1: Sent it
Person 2: Got it.
Person 1: You're unbelievable
```

This conversation revealed:
1. They're using a DES3 encryption for file transfers
2. The encryption key: `supersecretpassword123`
3. The file transfer port: 9002

## Extracting the Encrypted File
Following up on this information, I continued examining TCP streams until I found raw data being transferred over port 9002. This was likely the encrypted file mentioned in the conversation.

To extract this data:
1. I selected the TCP stream containing the file transfer
2. Changed the view to "Raw" format
3. Saved the data as "file.des3"

## Decrypting the File
Using the decryption information from the chat, I ran the following command:
```
openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
```

## Finding the Flag
Upon opening the decrypted `file.txt`, I found the flag:
```
picoCTF{nc_73115_411_0ee7267a}
```

## Conclusion
This challenge demonstrated several important forensics techniques:
- Analyzing network traffic to find human-readable information
- Following context clues to locate encrypted data
- Extracting binary data from packet captures
- Using cryptographic tools to decrypt data with known keys

The communication between the two individuals provided all the information needed to find and decrypt the file, highlighting how poor security practices (like discussing encryption keys in plaintext) can compromise sensitive information.
