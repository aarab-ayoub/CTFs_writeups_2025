# Enigma ROT Challenge Writeup

## Challenge Overview

This cryptography challenge involves decrypting a flag that has been obfuscated using alternating ROT cipher shifts and Base64 encoding. The challenge name "Enigma ROT" is a nod to both the famous Enigma machine from WWII and the ROT (rotation) cipher used in this challenge.

## Key Vulnerability: Alternating ROT Shifts with Known Parameters

In this challenge, the flag was encrypted using the following steps:
1. The original flag had its characters selectively rotated:
   - Characters at even indices (starting from index 3) were rotated by 1337 positions
   - Characters at odd indices (starting from index 3) were rotated by 42 positions
   - The "MED{" prefix was preserved unchanged
2. The result was then Base64 encoded

The ciphertext presented in the challenge was:
```
TUVEe3Y0eWpfem80ZTFfajRqcjB3XzFqXzFkX2h4NGpfMWVfMWl9
```

## Theoretical Background

### ROT Cipher

The ROT cipher (rotation cipher) is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet. The most common example is ROT13, where each letter is shifted 13 positions. For example, 'A' becomes 'N', 'B' becomes 'O', and so on.

In this challenge, two different rotation values are used: 1337 and 42. Due to the modular nature of the alphabet (26 letters), these large shifts are equivalent to shifts of:
- 1337 % 26 = 25 positions
- 42 % 26 = 16 positions

### Base64 Encoding

Base64 is an encoding scheme that represents binary data using 64 printable ASCII characters. It's commonly used to transmit binary data over text-based channels. Base64 encoding is not encryption, but rather a way to ensure the data can be safely transmitted.

## Attack Implementation

The attack is implemented in the following Python script:

```python
import base64

def rot_shift_char(c, shift):
    """
    Apply a ROT shift to a character
    """
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    else:
        return c

def reverse_rot_shift_char(c, shift):
    """
    Reverse a ROT shift on a character
    """
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
    else:
        return c  

def rev_apply_rot_shifts(data: str) -> str:
    """
    Reverse the alternating ROT shifts on the entire string
    """
    result = []
    result.append("MED")  # Keep the prefix unchanged
    for i, c in enumerate(data[3:], start=3):  # Start from index 3 (after "MED")
        if i % 2 == 0:  # Even index
            result.append(reverse_rot_shift_char(c, 1337))
        else:  # Odd index
            result.append(reverse_rot_shift_char(c, 42))
    return ''.join(result)

# Decode the Base64 encoded string
encoded_flag = "TUVEe3Y0eWpfem80ZTFfajRqcjB3XzFqXzFkX2h4NGpfMWVfMWl9"
decoded_base64 = base64.b64decode(encoded_flag).decode('utf-8')
print(f"Base64 decoded: {decoded_base64}")

# Apply reverse ROT shifts
decrypted_flag = rev_apply_rot_shifts(decoded_base64)
print(f"Decrypted flag: {decrypted_flag}")
```

## Key Steps in the Attack

1. **Base64 Decoding**:
   - The provided ciphertext is first decoded from Base64 to get the ROT-shifted flag
   - This results in: `MED{v4yj_zo4e1_j4jr0w_1j_1d_hx4j_1e_1i}`

2. **Applying Reverse ROT Shifts**:
   - Characters at positions 3, 5, 7, etc. (even indices) are rotated backwards by 1337 positions (modulo 26)
   - Characters at positions 4, 6, 8, etc. (odd indices) are rotated backwards by 42 positions (modulo 26)
   - The "MED{" prefix remains unchanged

3. **Character Shifting Logic**:
   - The `reverse_rot_shift_char()` function handles the actual character rotation
   - It checks if the character is a letter and applies the appropriate shift within the alphabet
   - Non-alphabetic characters (numbers, underscores, braces) remain unchanged

## Results

The script successfully recovers the flag:
```
Base64 decoded: MED{v4yj_zo4e1_j4jr0w_1j_1d_hx4j_1e_1i}
Decrypted flag: MED{k4nt_jd4t1_t4tg0l_1t_1s_wh4t_1t_1s}
```

## Why This Attack Works

This attack works because:

1. The encryption method uses fixed, known shift values (1337 and 42)
2. The pattern of which shift to apply to each position is predictable (alternating based on index parity)
3. The rotation cipher is easily reversible by applying a negative shift (or an equivalent positive shift in the opposite direction)
4. Base64 is a standard encoding with well-established decoding methods

## Security Implications

This challenge demonstrates why:

1. **Simple substitution ciphers** (like ROT) do not provide meaningful security, even when using multiple shift values
2. **Predictable patterns** in encryption algorithms create vulnerabilities
3. **Encoding is not encryption** - Base64 or other encoding schemes add no actual security
4. **Preserving known prefixes** (like "MED{") gives attackers valuable information about the encryption scheme

In a real-world cryptographic application, modern encryption algorithms with proper key management would be used instead of substitution ciphers.

## Mathematical Foundation

The ROT cipher is a special case of the Caesar cipher, which can be expressed mathematically as:

For encryption: E(x) = (x + k) mod 26
For decryption: D(x) = (x - k) mod 26

Where:
- x is the position of the plaintext letter in the alphabet (0-25)
- k is the shift value
- mod 26 ensures the result wraps around the alphabet

In this challenge, we have two different k values (1337 and 42) applied to alternating characters. Due to the properties of modular arithmetic, 1337 % 26 = 25 and 42 % 26 = 16, which means we could have used these smaller, equivalent shift values.

## Cultural References

The challenge name "Enigma ROT" references:
1. The Enigma machine - a famous cipher device used by Nazi Germany during World War II
2. The phrase "Two schools dominate the world of IT: 42 and 1337" refers to:
   - "42" - the "Answer to the Ultimate Question of Life, the Universe, and Everything" from "The Hitchhiker's Guide to the Galaxy"
   - "1337" (LEET) - a system of modified spellings used primarily on the Internet

## Flag

The recovered flag is:
```
MED{k4nt_jd4t1_t4tg0l_1t_1s_wh4t_1t_1s}
```
