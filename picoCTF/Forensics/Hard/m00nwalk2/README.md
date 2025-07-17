# m00nwalk2 Challenge Writeup

## Challenge Overview

**Challenge Name:** m00nwalk2  
**Category:** Forensics  
**Subject:** Revisit the last transmission. We think this transmission contains a hidden message. There are also some clues clue 1, clue 2, clue 3.  
**Hint:** Use the clues to extract the another flag from the .wav file

This challenge involves analyzing multiple audio files that contain SSTV (Slow Scan Television) transmissions and extracting hidden data using steganography techniques.

## Files Provided

- `message.wav` - Main transmission file
- `clue1.wav` - First clue file
- `clue2.wav` - Second clue file  
- `clue3.wav` - Third clue file

## Analysis

### 1. Understanding SSTV

SSTV (Slow Scan Television) is a method for transmitting images over radio frequencies. The audio files contain encoded image data that can be decoded back into visual information.

### 2. SSTV Decoding

Using the `sstv` tool to decode the audio files into images:

```bash
# Decode the main message
$ sstv -d message.wav -o message.png
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...   [###################################################################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!

# Decode clue 1
$ sstv -d clue1.wav -o clue1.png  
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Martin 1
[sstv] Decoding image...   [###################################################################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!

# Decode clue 2
$ sstv -d clue2.wav -o clue2.png
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 2
[sstv] Decoding image...   [###################################################################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!

# Decode clue 3
$ sstv -d clue3.wav -o clue3.png
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Martin 2
[sstv] Decoding image...   [###################################################################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
```

**Key observations:**
- Different SSTV modes were detected for each file:
  - `message.wav`: Scottie 1
  - `clue1.wav`: Martin 1
  - `clue2.wav`: Scottie 2
  - `clue3.wav`: Martin 2

### 3. Image Analysis

After decoding the SSTV transmissions, the resulting images contained:
- Various quotes and text snippets in the clue images
- **One of the clue images contained a password:** `hidden_stegosaurus`

### 4. Steganography Detection

Since the challenge mentioned extracting "another flag" and we found a password in the clues, this suggested that the main `message.wav` file contained hidden steganographic data.

Using `steghide` to investigate:

```bash
$ steghide info message.wav 
"message.wav":
  format: wave audio, PCM encoding
  capacity: 337.7 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "steganopayload12154.txt":
    size: 46.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

This confirmed that there was indeed hidden data embedded in the audio file, encrypted with AES-128 in CBC mode.

## Solution

### Step 1: Extract Hidden Data

Using the password found in the clue images:

```bash
$ steghide extract -sf message.wav -p hidden_stegosaurus
wrote extracted data to "steganopayload12154.txt".
```

### Step 2: Retrieve the Flag

```bash
$ cat steganopayload12154.txt
picoCTF{the_answer_lies_hidden_in_plain_sight}
```

## Flag

**`picoCTF{the_answer_lies_hidden_in_plain_sight}`**

## Solution Summary

1. **SSTV Decoding**: Used the `sstv` tool to convert audio transmissions back into images
2. **Clue Analysis**: Examined the decoded images to find hidden information (password)
3. **Steganography Detection**: Used `steghide` to detect hidden data in the main audio file
4. **Data Extraction**: Applied the discovered password to extract the encrypted payload
5. **Flag Recovery**: Retrieved the final flag from the extracted text file

## Key Takeaways

1. **Multi-Layer Analysis**: This challenge required understanding both SSTV transmission formats and steganography techniques
2. **Clue Integration**: The separate clue files weren't just distractors - they contained essential information (the password) needed to solve the main challenge
3. **Tool Combination**: Success required combining SSTV decoders with steganography tools
4. **Audio Steganography**: Demonstrated that audio files can contain hidden data beyond their apparent content
5. **Encryption Awareness**: The hidden data was encrypted (AES-128 CBC), showing the importance of proper password discovery

## Tools Used

- `sstv` - SSTV (Slow Scan Television) decoder for converting audio to images
- `steghide` - Steganography tool for hiding/extracting data from media files
- `cat` - Text file viewing

## Technical Details

### SSTV Modes Encountered
- **Scottie 1**: 320x256 resolution, used in message.wav and clue2.wav
- **Martin 1**: 320x256 resolution, used in clue1.wav  
- **Martin 2**: 320x256 resolution, used in clue3.wav

### Steganography Details
- **Encryption**: Rijndael-128 (AES-128) in CBC mode
- **Compression**: Yes (compressed payload)
- **Capacity**: 337.7 KB available in the audio file
- **Payload Size**: 46 bytes (the extracted flag text)

## Additional Notes

The challenge title "m00nwalk2" likely references the Apollo missions and radio communications, which historically used SSTV for transmitting images from space. This context fits perfectly with the SSTV transmission format used in the challenge.

The flag text "the_answer_lies_hidden_in_plain_sight" is quite fitting, as the SSTV images were "hidden in plain sight" within the audio files, and the final flag was hidden within the main transmission file.
