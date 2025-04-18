# Scan Surprise - Forensics Challenge Writeup

## Challenge Description
I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?

You can download the challenge files here:
* challenge.zip

The same files are accessible via SSH here:
`ssh -p 61114 ctf-player@atlas.picoctf.net`
Using the password `84b12bae`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

## Hints
1. QR codes are a way of encoding data. While they're most known for storing URLs, they can store other things too.
2. Mobile phones have included native QR code scanners in their cameras since version 8 (Oreo) and iOS 11.
3. If you don't have access to a phone, you can also use zbar-tools to convert an image to text.

## Solution

This challenge provides a zip file containing a QR code image that we need to decode to find the flag.

### Method 1: Connect via SSH and Scan the QR Code with a Phone

First, I connected to the provided SSH server:
```bash
ssh -p 61114 ctf-player@atlas.picoctf.net
```

After accepting the fingerprint with `yes` and entering the password `84b12bae`, I listed the contents of the directory:
```bash
ls
```

This revealed a file named `flag.png`, which is a QR code image. I then used my phone's camera to scan the QR code displayed on the screen, which directly revealed the flag:
```
picoCTF{p33k_@_b00_0194a007}
```

### Method 2: Using zbarimg (Command-Line QR Code Reader)

Alternatively, as mentioned in the hints, we can use the `zbarimg` tool from the zbar-tools package to decode the QR code:
```bash
ctf-player@challenge:~/drop-in$ zbarimg flag.png
Connection Error (Failed to connect to socket /var/run/dbus/system_bus_socket: No such file or directory)
Connection Null
QR-Code:picoCTF{p33k_@_b00_0194a007}
scanned 1 barcode symbols from 1 images in 0 seconds
```

Despite the connection error messages (which are unrelated to the functionality), the tool successfully decoded the QR code and displayed the flag.

## Flag
`picoCTF{p33k_@_b00_0194a007}`

## Tools Used
- SSH client
- Mobile phone with QR code scanning capability
- zbarimg (from zbar-tools package)

## Learning Points
- QR codes can encode more than just URLs - they can contain plain text, including flags
- There are multiple ways to scan QR codes:
  - Using a mobile phone camera
  - Using command-line tools like zbarimg
- Basic understanding of SSH connections
