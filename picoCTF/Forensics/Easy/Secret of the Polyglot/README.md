# Secret of the Polyglot - Forensics Challenge Writeup

## Challenge Description
The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?

## Hint
This problem can be solved by just opening the file in different ways.

## Solution

In this challenge, we're presented with a file that appears to be a polyglot - a file that can be interpreted as multiple file formats simultaneously.

### Step 1: Initial Investigation

First, I examined the file's hex data using the `xxd` command:

```bash
xxd flag2of2-final.pdf       
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0032 0000 0032 0806 0000 001e 3f88  ...2...2......?.
00000020: b100 0001 8569 4343 5049 4343 2070 726f  .....iCCPICC pro
```

The interesting discovery here is that despite having a `.pdf` extension, the file starts with the PNG file signature (`89 50 4E 47`) rather than the typical PDF header. This confirms that the file is indeed a polyglot that can be interpreted as both a PNG image and a PDF document.

### Step 2: Opening as a PDF

When opening the file as a PDF (using any PDF viewer), we can see that it contains the second part of the flag:

```
1n_pn9_&_pdf_90974127}
```

### Step 3: Opening as a PNG

Since the file also has PNG headers, I changed the extension to `.png` and opened it as an image. This revealed the first part of the flag:

```
picoCTF{f1u3n7_
```

### Step 4: Combining the Flag Parts

By combining both parts, we get the complete flag:

```
picoCTF{f1u3n7_1n_pn9_&_pdf_90974127}
```

## Flag
`picoCTF{f1u3n7_1n_pn9_&_pdf_90974127}`

## Tools Used
- xxd (hex dumping tool)
- PDF viewer
- Image viewer

## Learning Points
- A polyglot file can be valid in multiple file formats simultaneously
- File headers are more important than extensions for determining a file's format
- Different viewers/programs will interpret the same file differently based on how they process it
- Forensic challenges often require examining files in different ways to reveal hidden information
