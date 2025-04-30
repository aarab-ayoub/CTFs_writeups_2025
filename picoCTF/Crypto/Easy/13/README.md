# CTF Challenge: ROT13

## Challenge Description
Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}`

**Hint:** This can be solved online if you don't want to do it by hand!

## Solution Approach

### Understanding ROT13

ROT13 (rotate by 13 places) is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet. It's a special case of the Caesar cipher, developed in ancient Rome.

For example:
- 'A' becomes 'N'
- 'B' becomes 'O'
- 'Z' becomes 'M'

The algorithm is symmetric, meaning applying ROT13 twice returns the original text, making it a convenient method for hiding text.

### Decoding the Cipher

The challenge provides us with a ciphertext: `cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}`

Since the challenge directly hints at ROT13, we can decode it by shifting each alphabetic character by 13 positions:

1. **Manual method:** For each character, count 13 letters forward in the alphabet (or 13 backward, as they're equivalent in ROT13)
2. **Online tools:** Use a tool like CyberChef which has ROT13 as a built-in operation
3. **Command line:** Use tools like `tr` in Unix systems

### Using CyberChef

I opted to use CyberChef for quick decoding:

1. Go to [CyberChef](https://gchq.github.io/CyberChef/)
2. Add the "ROT13" operation
3. Input the ciphertext: `cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}`
4. Execute the operation

The result immediately revealed the flag:
```
picoCTF{not_too_bad_of_a_problem}
```

## Alternative Methods

### Python Script
```python
def rot13(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

ciphertext = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
print(rot13(ciphertext))
```

### Command Line with tr
```bash
echo "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

## Tools Used
- CyberChef - Online cryptographic toolkit

## Conclusion
This challenge introduces basic cryptography concepts through ROT13, one of the simplest classical ciphers. While extremely easy to break, ROT13 is still used in various contexts to obscure text from casual viewing. The challenge demonstrates how readily accessible online tools can quickly decipher such basic encryption methods.

## Flag
`picoCTF{not_too_bad_of_a_problem}`
