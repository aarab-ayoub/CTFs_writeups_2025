# RED Challenge Writeup

## Challenge Overview
**Challenge Name:** RED  
**Description:** RED, RED, RED, RED

**Hints:**
- The picture seems pure, but is it though?
- Red?Ged?Bed?Aed?
- Check whatever Facebook is called now.

## Initial Analysis

We were given a PNG image file called "red.png". Given the challenge name and the hints, it was clear that the image contained some hidden data.

## Step 1: Checking Metadata

First, I used `exiftool` to examine the metadata of the image:

```bash
$ exiftool red.png
ExifTool Version Number         : 13.00
File Name                       : red.png
Directory                       : .
File Size                       : 796 bytes
File Modification Date/Time     : 2025:04:15 19:23:48+01:00
File Access Date/Time           : 2025:04:15 19:23:49+01:00
File Inode Change Date/Time     : 2025:04:15 19:23:48+01:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 128
Image Height                    : 128
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Poem                            : Crimson heart, vibrant and bold,.Hearts flutter at your sight..Evenings glow softly red,.Cherries burst with sweet life..Kisses linger with your warmth..Love deep as merlot..Scarlet leaves falling softly,.Bold in every stroke.
Image Size                      : 128x128
Megapixels                      : 0.016
```

This revealed a poem in the metadata with a red/crimson theme, matching the challenge name. However, this wasn't the flag.

## Step 2: Steganography Analysis

The hint "Check whatever Facebook is called now" (Meta) suggested looking for metadata or using steganography tools. I decided to use `zsteg`, a tool for detecting hidden data in PNG and BMP files:

```bash
$ zsteg red.png
meta Poem           .. text: "Crimson heart, vibrant and bold,\nHearts flutter at your sight.\nEvenings glow softly red,\nCherries burst with sweet life.\nKisses linger with your warmth.\nLove deep as merlot.\nScarlet leaves falling softly,\nBold in every stroke."
b1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ=="
b1,rgba,msb,xy      .. file: OpenPGP Public Key
b2,g,lsb,xy         .. text: "ET@UETPETUUT@TUUTD@PDUDDDPE"
b2,rgb,lsb,xy       .. file: OpenPGP Secret Key
b2,bgr,msb,xy       .. file: OpenPGP Public Key
b2,rgba,lsb,xy      .. file: OpenPGP Secret Key
b2,rgba,msb,xy      .. text: "CIkiiiII"
b2,abgr,lsb,xy      .. file: OpenPGP Secret Key
b2,abgr,msb,xy      .. text: "iiiaakikk"
b3,rgba,msb,xy      .. text: "#wb#wp#7p"
b3,abgr,msb,xy      .. text: "7r'wb#7p"
b4,b,lsb,xy         .. file: 0421 Alliant compact executable not stripped
```

This revealed much more interesting data! In the `b1,rgba,lsb,xy` output, I found a string that appeared to be Base64 encoded. The string was repeated four times, which aligned with the hint "Red?Ged?Bed?Aed?" suggesting four instances of something.

## Step 3: Decoding the Base64 String

I isolated one instance of the Base64 string:
```
cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==
```

And decoded it:
```bash
$ echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```

## The Flag

The flag for this challenge is:
```
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```

## Conclusion

This challenge emphasized the importance of steganography in CTF competitions. The image contained hidden data in its LSB (Least Significant Bit) encoding, which is a common steganography technique. The repeated Base64 string was the encoded flag, and once decoded, we obtained our solution.

The hints were quite helpful:
- "The picture seems pure, but is it though?" - Indicated hidden data
- "Red?Ged?Bed?Aed?" - Hinted at the four repetitions of the encoded flag
- "Check whatever Facebook is called now" - Pointed to Meta/metadata analysis

Tools like `exiftool` and `zsteg` are invaluable for these types of challenges, allowing us to examine both the metadata and perform steganographic analysis on images.
