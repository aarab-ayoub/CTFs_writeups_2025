# CTF Challenge: Vigenere

## Challenge Description
Can you decrypt this message? Decrypt this message using this key "CYLAB".

## Solution Approach

### Understanding Vigenere Cipher

The Vigenere cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. Unlike simple substitution ciphers that use the same key for all letters, Vigenere uses different Caesar cipher shifts based on the letters of a keyword.

How it works:
1. A keyword is repeated until it matches the length of the plaintext
2. Each letter of the keyword determines the shift amount for the corresponding letter in the plaintext
3. For decryption, the process is reversed

### Given Information
- Encrypted text: `rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}`
- Key: `CYLAB`

### Decryption Process

The Vigenere cipher only encrypts alphabetic characters, leaving numbers and special characters unchanged. For this challenge, we need to:

1. Apply the key `CYLAB` to the encrypted text
2. Repeat the key to match the length of the encrypted text
3. For each alphabetic character in the ciphertext, shift it backward according to the corresponding key letter

#### Manual Decryption Example:
- First letter of ciphertext: `r`
- First letter of key: `C` (shift value of 2)
- Shift `r` backward by 2 positions: `r` - 2 = `p`

#### Using CyberChef

For efficiency, I used CyberChef's built-in Vigenere decoder:

1. Go to [CyberChef](https://gchq.github.io/CyberChef/)
2. Add the "Vigenère Decode" operation
3. Input the encrypted text: `rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}`
4. Set the key to: `CYLAB`
5. Execute the operation


The result revealed the decrypted flag:
```
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_d85729g7}
```

### Alternative Python Solution

For those interested in a programmatic approach, here's a Python script that can be used to decrypt the Vigenere cipher:

```python
def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    
    for char in ciphertext:
        # Only decrypt alphabetic characters
        if char.isalpha():
            # Calculate shift based on current key character
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            
            # Handle uppercase and lowercase differently
            if char.isupper():
                decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                
            plaintext += decrypted
            key_index += 1
        else:
            # Keep non-alphabetic characters as is
            plaintext += char
            
    return plaintext

# Encrypted flag and key
encrypted = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}"
key = "CYLAB"

# Decrypt the flag
flag = vigenere_decrypt(encrypted, key)
print(flag)
```

## Tools Used
- CyberChef - Online cryptographic toolkit with Vigenere decoder

## Conclusion
This challenge demonstrates the application of a classical polyalphabetic substitution cipher, the Vigenere cipher. While more secure than simple substitution ciphers like Caesar, Vigenere is still vulnerable when the key is known. This exercise highlighted the importance of key secrecy in cryptographic systems and provided practice with a historically significant encryption method.

## Flag
`picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_d85729g7}`
