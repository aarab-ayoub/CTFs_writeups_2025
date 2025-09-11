
## Vowel Cipher Challenge

### Challenge Overview

The first challenge involves a custom cipher called "Vowel Consonant Cipher" where vowels and consonants are treated differently during the encryption process.

### Challenge Description

"Five privileged letters always move ahead, while the others fall behind - their journey's length depends on their birth order"

This cryptic description refers to the five vowels (a, e, i, o, u) being "privileged" and moving forward in the alphabet, while consonants move backward. The "journey's length" (shift amount) depends on the position of the character in the original text.

### Algorithm Analysis

The provided code implements both encryption and decryption functions:

```python
def vowel_consonant_cipher(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    pos = 0  
    
    for char in text:
        if not char.isalpha():
            result.append(char)  # Non-alphabetic characters remain unchanged
            continue
            
        pos += 1  # Position counter increments for each alphabetic character
        original_lower = char.lower()
        base = ord('a') if char.islower() else ord('A')  # Preserve case
        original_pos = ord(original_lower) - ord('a')  # Position in alphabet (0-25)
        
        if original_lower in vowels:
            new_pos = (original_pos + pos) % 26  # Vowels shift forward by position count
        else:
            new_pos = (original_pos - pos) % 26  # Consonants shift backward by position count
            
        result.append(chr(base + new_pos))
    
    return ''.join(result)
```

Key features of this algorithm:

1. **Progressive Shift**: The shift value increases with each alphabetic character in the input
2. **Differential Treatment**: Vowels and consonants shift in opposite directions
3. **Case Preservation**: The cipher maintains the original case of letters
4. **Non-Alphabetic Preservation**: Symbols, numbers, and special characters remain unchanged

### Decryption Analysis

The decryption algorithm requires careful handling of the progressive shift and determining whether a character was originally a vowel or consonant:

```python
def vowel_consonant_decipher(ciphertext):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    pos = 0
    
    for char in ciphertext:
        if not char.isalpha():
            result.append(char)
            continue
            
        pos += 1
        encrypted_lower = char.lower()
        base = ord('a') if char.islower() else ord('A')
        encrypted_pos = ord(encrypted_lower) - ord('a')
        
        # Try assuming the character was a vowel
        vowel_original_pos = (encrypted_pos - pos) % 26
        vowel_original_char = chr(ord('a') + vowel_original_pos)
        
        # Determine if the assumption is correct
        if vowel_original_char in vowels:
            new_pos = vowel_original_pos
        else:
            # Otherwise assume it was a consonant
            consonant_original_pos = (encrypted_pos + pos) % 26
            new_pos = consonant_original_pos
            
        result.append(chr(base + new_pos))
    
    return ''.join(result)
```

The decryption algorithm is more complex because it must:
1. Try both possible transformations (vowel and consonant)
2. Determine which one produces a valid result
3. Apply the correct inverse transformation

### Challenge Solution

The code provided shows both the encryption and decryption process:

```
Original: MED{v0w3ls_f0rw4rd_c0ns0n4nts_b4ckw4rd}
Encrypted: LGA{r0r3fl_x0im4gr_p0zd0x4wbz_h4hoz4te}
Decrypted: MED{v0w3ls_f0rw4rd_c0ns0n4nts_b4ckw4rd}
```

The flag is: **MED{v0w3ls_f0rw4rd_c0ns0n4nts_b4ckw4rd}**

### Key Observations

1. The cipher gets progressively more complex as the text gets longer, since the shift value increases
2. The algorithm requires knowledge of whether a character was originally a vowel or consonant
3. The hint "Five privileged letters always move ahead" nicely summarizes the core mechanic

## Challenge 2: Base58 Decoding Challenge

### Challenge Overview

This challenge involves decoding a Base58-encoded string to reveal a flag that has been encrypted using a different method.

### Initial Decoding

The command provided shows:
```
echo rcqFdFfdbK7BdWZsxB44t2nDL1HLMR5kvf4T5TDiPeWWqkxmMpBoAtDTNB6DGDSSSh2C | base58 -d
```

This decodes the Base58 string to: `Encrypted: LGA{r0r3fl_x0im4gr_p0zd0x4wbz_h4hoz4te}%`

### Connection to Challenge 1

Interestingly, the decoded output `LGA{r0r3fl_x0im4gr_p0zd0x4wbz_h4hoz4te}` matches the encrypted text from the first challenge exactly.

### Solution

Since we know this string is encrypted with the Vowel Consonant Cipher from Challenge 1, we can apply the decryption function to reveal the original flag:

```python
encrypted = "LGA{r0r3fl_x0im4gr_p0zd0x4wbz_h4hoz4te}"
decrypted = vowel_consonant_decipher(encrypted)
print("Decrypted:", decrypted)
```

Result:
```
Decrypted: MED{v0w3ls_f0rw4rd_c0ns0n4nts_b4ckw4rd}
```

### Combined Solution Path

The complete solution path for Challenge 2:

1. Decode the Base58 string to get `LGA{r0r3fl_x0im4gr_p0zd0x4wbz_h4hoz4te}`
2. Identify that this is encrypted with the Vowel Consonant Cipher
3. Apply the decryption algorithm to reveal `MED{v0w3ls_f0rw4rd_c0ns0n4nts_b4ckw4rd}`

## Cryptographic Techniques Used

1. **Custom Substitution Cipher**: The Vowel Consonant Cipher is a novel substitution cipher with position-dependent shifts
2. **Base58 Encoding**: A binary-to-text encoding scheme that avoids similar-looking characters
3. **Chained Encryption**: Challenge 2 uses multiple layers of encryption/encoding

## Educational Value

These challenges demonstrate:

1. **Progressive Shift Ciphers**: How ciphers can incorporate positional information
2. **Character-Dependent Transformations**: How encryption can apply different rules to different character types
3. **Layered Encryption**: How multiple encryption layers can be combined
4. **Decryption Logic**: How to reason about and reverse complex custom encryption schemes

## Flag

For both challenges, the flag is:
**MED{v0w3ls_f0rw4rd_c0ns0n4nts_b4ckw4rd}**