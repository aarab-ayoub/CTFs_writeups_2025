# CTF Challenge: interencdec

## Challenge Description
Can you get the real meaning from this file. Download the file here.

**Hint:** Engaging in various decoding processes is of utmost importance

## Solution Approach

### Step 1: Examining the File
Upon downloading and examining the provided file, I found a string that appeared to be encoded:

```
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6YzRNalV3YUcxcWZRPT0nCg==
```

The string ends with `==`, which is a common indicator of Base64 encoding due to the padding characters.

### Step 2: First Layer - Base64 Decoding
Base64 is a common encoding scheme that converts binary data to ASCII text format. I decoded the string using Base64:

```bash
echo "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6YzRNalV3YUcxcWZRPT0nCg==" | base64 -d
```

Result:
```
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzc4MjUwaG1qfQ=='
```

### Step 3: Second Layer - Another Base64 Decoding
The output from the first decoding appears to be another Base64 encoded string. I decoded it again:

```bash
echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzc4MjUwaG1qfQ==" | base64 -d
```

Result:
```
wpjvJAM{jhlzhy_k3jy9wa3k_78250hmj}
```

### Step 4: Final Layer - Caesar Cipher
The output now resembles a flag format but with scrambled letters. The prefix `wpjvJAM` should be `picoCTF`, suggesting a Caesar cipher (as hinted by "jhlzhy" which decodes to "caesar").

While a standard ROT13 cipher shifts letters by 13 positions, this one required a different shift. After trying different rotation values, I found that ROT19 (shifting by 19 positions) gave the correct flag:

```
picoCTF{caesar_d3cr9pt3d_78250afc}
```

I confirmed this was the right shift because:
- 'w' + 19 = 'p'
- 'p' + 19 = 'i'
- 'j' + 19 = 'c'
- 'v' + 19 = 'o'

And so on, which correctly transforms "wpjvJAM" to "picoCTF".

## Tools Used
- Base64 decoder (command line or online tool)
- Caesar cipher decoder with adjustable rotation

## CyberChef Solution
This entire solution can be implemented as a single recipe in CyberChef:
1. Base64 Decode (first layer)
2. Base64 Decode (second layer)
3. ROT19 (Caesar cipher with shift of 19)

## Conclusion
This challenge demonstrated the concept of layered encoding - a common technique where data is encoded multiple times using different methods. The solution required:
1. Recognizing Base64 encoding (twice)
2. Identifying and applying the correct Caesar cipher rotation

The hint about "various decoding processes" was accurate, as we needed to apply different decoding methods sequentially to reveal the flag.

## Flag
`picoCTF{caesar_d3cr9pt3d_78250afc}`
