# Enhance! Writeup

## Challenge Information
- **Name**: Enhance!
- **Description**: Download this image file and find the flag.
- **Hints**: None provided

## Understanding the Challenge

For this challenge, we're provided with an SVG (Scalable Vector Graphics) image file. The name "Enhance!" suggests we might need to look more closely at the image or its components to find hidden information.

SVG files are actually XML-based text files that describe vector graphics. This means they can be opened and read like any text file, which could be useful for finding hidden information.

## Initial Analysis

Opening the SVG file in a text editor reveals that it's an XML file with various elements defining the image. Since we're looking for a flag with the format `picoCTF{...}`, it's a good idea to examine the content for any text that might contain the flag.

When examining the raw XML content of the SVG file, I noticed it contains `<text>` and `<tspan>` elements, which are used to define text within an SVG image.

## Solution Approach

Upon closer inspection of the SVG file, I found that the flag is actually hidden in several `<tspan>` elements within the file. Each `<tspan>` element contains a fragment of the flag.

To extract these fragments, I used the following command:

```bash
cat drawing.flag.svg | grep tspan
```

This command searches for all lines containing "tspan" in the SVG file.

The output revealed:

```
       id="text3723"><tspan
         id="tspan3748">p </tspan><tspan
         id="tspan3754">i </tspan><tspan
         id="tspan3756">c </tspan><tspan
         id="tspan3758">o </tspan><tspan
         id="tspan3760">C </tspan><tspan
         id="tspan3762">T </tspan><tspan
         id="tspan3764">F { 3 n h 4 n </tspan><tspan
         id="tspan3752">c 3 d _ a a b 7 2 9 d d }</tspan></text>
```

From this output, I could piece together the individual characters to form the complete flag:

```
picoCTF{3nh4nc3d_aab729dd}
```

## Flag

The flag for this challenge is:
```
picoCTF{3nh4nc3d_aab729dd}
```

## Reflection

This challenge demonstrates the importance of understanding file formats and looking beyond the visible content of files. While the SVG appeared to be just an image file, it actually contained hidden text that wasn't easily visible when viewing the image normally.

The name "Enhance!" was quite fitting, as we needed to "enhance" our view of the file by examining its raw content rather than just viewing it as an image. This is a common technique in CTF challenges and digital forensics - always examine files in multiple ways, as information can be hidden in unexpected places.

This challenge also highlights how knowledge of command-line tools like `cat` and `grep` can be invaluable in CTF competitions for quickly searching through files to find relevant information
