# CTF Challenge: hideme

## Challenge Description
Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.

## Solution Approach

### Step 1: Initial File Analysis
First, I examined the provided image file to gather basic information:

```bash
file flag.png
```

Output:
```
flag.png: PNG image data, 512 x 504, 8-bit/color RGBA, non-interlaced
```

### Step 2: Metadata Examination
Next, I checked the metadata of the image using ExifTool:

```bash
exiftool flag.png
```

Output:
```
ExifTool Version Number         : 13.00
File Name                       : flag.png
Directory                       : .
File Size                       : 43 kB
File Modification Date/Time     : 2025:04:29 03:19:31+01:00
File Access Date/Time           : 2025:04:29 03:19:31+01:00
File Inode Change Date/Time     : 2025:04:29 03:19:31+01:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 512
Image Height                    : 504
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                       : 512x504
Megapixels                      : 0.258
```

The important clue here was the warning: `[minor] Trailer data after PNG IEND chunk`. This suggests hidden data after the PNG's normal end marker.

### Step 3: Analyzing File Structure
I used Binwalk to analyze the file structure:

```bash
binwalk flag.png
```

Output:
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2876, uncompressed size: 3029, name: secret/flag.png
42915         0xA7A3          End of Zip archive, footer length: 22
```

This confirmed the file contained hidden data - specifically a ZIP archive that includes another image named `flag.png` in a `secret` directory.

### Step 4: Extracting Hidden Content
I extracted the hidden content using:

```bash
binwalk -e flag.png
```

This created an output directory containing the extracted data.

### Step 5: Finding the Flag
In the extracted data, I navigated to the `secret` folder and found another image that contained the flag:

```
picoCTF{Hiddinng_An_Imag3_Within_@n_Ima9e_d55982e8}
```

## Conclusion
This challenge demonstrates a basic steganography technique where a ZIP archive containing another image was appended to a PNG file after its end marker (IEND chunk). The technique is simple but effective for hiding data within images.

## Tools Used
- `file` - File type identification
- `exiftool` - Metadata analysis
- `binwalk` - Binary file analysis and extraction

## Flag
`picoCTF{Hiddinng_An_Imag3_Within_@n_Ima9e_d55982e8}`
