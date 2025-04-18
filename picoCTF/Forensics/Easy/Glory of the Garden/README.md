# Glory of the Garden - Forensics Challenge Writeup

## Challenge Overview

**Challenge Name:** Glory of the Garden  
**Description:** This garden contains more than it seems.  
**Hint:** What is a hex editor?

## Initial Analysis

The challenge provides an image file named `garden.jpg` and a hint suggesting that we should look at the file using a hex editor. This indicates that there might be hidden data within the raw bytes of the image file.

## Solution Approach

Since the hint explicitly mentions a hex editor, I decided to examine the raw hexadecimal data of the image. This is a common technique in forensics challenges where flags or hidden messages are sometimes appended to the end of the file after the actual image data.

I used the `xxd` command-line utility, which is a hex dumper that displays the contents of a file in hexadecimal:

```bash
$ xxd garden.jpg
```

After scrolling through the output, I found something interesting at the very end of the file:

```
00230550: a2bb bdac 9687 98e4 d3b2 e87f ffd9 4865  ..............He
00230560: 7265 2069 7320 6120 666c 6167 2022 7069  re is a flag "pi
00230570: 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  coCTF{more_than_
00230580: 6d33 3374 735f 7468 655f 3379 3336 3537  m33ts_the_3y3657
00230590: 4261 4232 437d 220a                      BaB2C}".
```

The hex dump reveals that right after the JPEG end marker (`ffd9`), there is a plain text message:

> Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"

## Finding the Flag

The flag is clearly visible in the hex dump and is formatted as expected for a picoCTF challenge:

```
picoCTF{more_than_m33ts_the_3y3657BaB2C}
```

## Technical Explanation

This challenge demonstrates a basic steganography technique where data is hidden within a file without affecting its primary function. In this case:

1. The JPEG image ends with the marker `ffd9` (visible in the hex dump)
2. Text data was appended after this marker
3. Since most image viewers stop processing the file once they reach the end marker, the additional data doesn't affect how the image displays
4. However, when examining the raw file data with a hex editor, we can see the hidden message

## Conclusion

This challenge introduces a fundamental concept in digital forensics: files may contain hidden data that isn't visible when viewing the file normally. Using appropriate tools like hex editors is essential for discovering such hidden information.

The challenge name "Glory of the Garden" was a hint itself, suggesting that there was more to the garden image than initially met the eye - you had to look "beneath the surface" to find the hidden treasure (the flag).
