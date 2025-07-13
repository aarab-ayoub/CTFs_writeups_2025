# Webnet 1 - PicoCTF Challenge Writeup

## Challenge Information
- **Name**: Webnet 1
- **Category**: Forensics / Network Analysis + Steganography
- **Difficulty**: Hard
- **Description**: We found this packet capture and key. Recover the flag.
- **Files**: 
  - Packet capture file (.pcap/.pcapng)
  - TLS private key file
- **Hints**:
  1. Try using a tool like Wireshark.
  2. How can you decrypt the TLS stream?

## Solution Overview

This challenge builds upon TLS decryption techniques by combining network forensics with steganography. After decrypting the TLS traffic, we need to extract files from the HTTP streams and analyze them for hidden data using steganography techniques.

## Step-by-Step Solution

### Step 1: Configure TLS Decryption in Wireshark
Following the same process as Webnet 0:

1. Open the packet capture in Wireshark
2. Go to **Edit** → **Preferences** → **Protocols** → **TLS**
3. Configure **RSA keys list** with:
   - **IP Address**: Server's IP from the capture
   - **Port**: 443 (HTTPS)
   - **Protocol**: http
   - **Key File**: The provided private key file

### Step 2: Analyze Decrypted HTTP Traffic
After applying the RSA key configuration, the encrypted TLS streams become readable HTTP traffic. Browse through the decrypted streams to identify interesting requests and responses.

### Step 3: Locate Image Download
Search through the HTTP streams for file downloads, particularly image files. Look for:
- HTTP GET requests for image files (`.jpg`, `.png`, `.gif`, etc.)
- HTTP responses with image content types
- Large response bodies that might contain binary data

In this case, an HTTP GET request for an image file was found in the decrypted traffic.

### Step 4: Extract the Image File
From the HTTP response containing the image:

1. **Using Wireshark GUI**:
   - Right-click on the HTTP response packet
   - Select **Follow** → **HTTP Stream**
   - In the stream window, select **Raw** format
   - Save the response body to a file (e.g., `vulture.jpg`)

2. **Alternative Method**:
   - Use **File** → **Export Objects** → **HTTP**
   - Select the image file from the list
   - Save it to your filesystem

### Step 5: Initial Image Analysis
Open the extracted image file to verify it's a valid image:

```bash
# View the image
xdg-open vulture.jpg
# or
display vulture.jpg
```

The image appears to be a normal picture with no obvious hidden information visible.

### Step 6: Steganography Analysis
Since the image doesn't contain obvious clues, analyze it for hidden data using steganography techniques:

#### Using ExifTool
ExifTool can extract metadata from image files, including custom fields where data might be hidden:

```bash
exiftool vulture.jpg
```

**Output:**
```
ExifTool Version Number         : 13.10
File Name                       : vulture.jpg
Directory                       : .
File Size                       : 70 kB
File Modification Date/Time     : 2025:07:13 20:09:24+01:00
File Access Date/Time           : 2025:07:13 20:09:25+01:00
File Inode Change Date/Time     : 2025:07:13 20:09:24+01:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 1
Y Resolution                    : 1
Resolution Unit                 : None
Artist                          : picoCTF{honey.roasted.peanuts}
Y Cb Cr Positioning             : Centered
Profile CMM Type                : Little CMS
```

### Step 7: Flag Discovery
The flag is hidden in the **Artist** field of the image's EXIF metadata:
```
Artist                          : picoCTF{honey.roasted.peanuts}
```

## Key Concepts Learned

### Network Forensics
1. **TLS Decryption**: Using private keys to decrypt HTTPS traffic
2. **HTTP Object Extraction**: Retrieving files from network captures
3. **Protocol Analysis**: Understanding layered network communications

### Steganography
1. **EXIF Metadata**: Hidden data in image file metadata
2. **Steganography Tools**: Using specialized tools to find hidden information
3. **Multi-layer Analysis**: Combining network and file analysis techniques

### File Analysis
1. **Image Formats**: Understanding JPEG structure and metadata
2. **Metadata Fields**: Custom fields that can store arbitrary data
3. **Tool Usage**: Leveraging tools like ExifTool for forensic analysis

## Tools Used
- **Wireshark** - Network protocol analyzer and TLS decryption
- **ExifTool** - Metadata extraction and analysis tool
- **Standard file viewers** - For initial image verification

## Alternative Steganography Analysis Methods

### 1. Strings Command
```bash
strings vulture.jpg | grep -i pico
```

### 2. Binwalk
```bash
binwalk vulture.jpg
```

### 3. Steghide
```bash
steghide extract -sf vulture.jpg
```

### 4. Stegsolve
```bash
java -jar stegsolve.jar vulture.jpg
```

### 5. Hexdump Analysis
```bash
hexdump -C vulture.jpg | grep -i pico
```

## EXIF Metadata Fields
Common EXIF fields where data might be hidden:
- **Artist**: Creator/author information
- **Copyright**: Copyright information  
- **Comment**: General comments
- **Description**: Image description
- **Software**: Software used to create the image
- **User Comment**: User-defined comments

## Security Implications

### Network Security
1. **TLS Inspection**: Organizations can decrypt their own TLS traffic for monitoring
2. **Key Management**: Proper protection of private keys is crucial
3. **Forward Secrecy**: Modern TLS prevents retroactive decryption

### Steganography
1. **Data Exfiltration**: Hiding data in image metadata is a common technique
2. **Metadata Scrubbing**: Many platforms automatically strip EXIF data
3. **Detection Methods**: Automated tools can scan for hidden data

## Workflow Summary

```
1. Packet Capture → Wireshark → TLS Decryption
2. Decrypted HTTP → File Extraction → Image File
3. Image Analysis → Steganography Tools → Hidden Data
4. EXIF Metadata → Flag Discovery
```

## Additional Analysis Commands

### Complete EXIF Analysis
```bash
# Detailed EXIF information
exiftool -a -u -g1 vulture.jpg

# Extract all metadata
exiftool -all= -overwrite_original vulture.jpg

# Search for specific strings
exiftool vulture.jpg | grep -i flag
```

### File Format Analysis
```bash
# Check file type
file vulture.jpg

# View file headers
head -c 100 vulture.jpg | hexdump -C
```

## Flag
```
picoCTF{honey.roasted.peanuts}
```

## Conclusion

Webnet 1 demonstrates the multi-layered nature of modern digital forensics, combining network analysis, cryptography, and steganography. The challenge shows how attackers might hide data in seemingly innocent image files transmitted over encrypted channels. 

The progression from network traffic analysis to file extraction to steganography analysis represents a realistic forensic workflow. The use of EXIF metadata to hide the flag is particularly clever, as it's a common technique used by malware and data exfiltration tools.

This challenge emphasizes the importance of:
1. Comprehensive analysis of all extracted artifacts
2. Understanding multiple forensic domains (network, file, steganography)
3. Using appropriate tools for each analysis phase
4. Not stopping at surface-level examination of recovered files
