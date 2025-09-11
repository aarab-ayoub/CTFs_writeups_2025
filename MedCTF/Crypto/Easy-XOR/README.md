# Easy XOR Challenge Writeup

## Challenge Overview

This cryptography challenge involves decrypting a flag that has been obfuscated using a combination of XOR encryption and multiple rounds of base32 encoding.

## Key Vulnerability: Simple XOR with Known Key

In this challenge, the flag was encrypted using the following steps:
1. The original flag was XORed with a fixed key "MED"
2. The result was then base32 encoded 5 times in succession

To solve this challenge, we need to reverse these operations:
1. Base32 decode the ciphertext 5 times
2. XOR the result with the key "MED" to recover the original flag

## Theoretical Background

### XOR Encryption

XOR (exclusive OR) is a bitwise operation that takes two equal-length bit patterns and produces a result where the bits are set to 1 only when the corresponding input bits are different. In cryptography, XOR is commonly used as a simple encryption method:

```
Encryption: ciphertext = plaintext XOR key
Decryption: plaintext = ciphertext XOR key
```

A key property of XOR is that applying the same key twice cancels out the operation:
```
(plaintext XOR key) XOR key = plaintext
```

When the key is shorter than the plaintext, it's typically repeated cyclically.

### Base32 Encoding

Base32 is a notation system used to represent binary data using a set of 32 ASCII characters (A-Z and 2-7). Each 5 bits of input data is represented as a single character in the output. Base32 encoding increases the size of the data by approximately 60%.

Multiple rounds of base32 encoding exponentially increase the length of the ciphertext, making manual decoding impractical and obfuscating the original content.

## Attack Implementation

The attack is implemented in the following Python script:

```python
import base64

def xor_with_key(data: str, key: str) -> str:
    """XOR each character of data with the corresponding character in the key."""
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def decode_challenge(encoded_data: str) -> str:
    """
    Decode the challenge by:
    1. Adding padding if necessary
    2. Base32 decoding 5 times
    3. XOR-ing with the key "MED"
    """
    # Add padding if necessary
    while len(encoded_data) % 8 != 0:
        encoded_data += '='
    
    # Base32 decode 5 times
    decoded = encoded_data.encode('utf-8')
    for i in range(5):
        try:
            decoded = base64.b32decode(decoded)
        except Exception as e:
            print(f"Error during decoding (iteration {i+1}): {e}")
            return None
    
    # XOR with key "MED"
    try:
        decoded_str = decoded.decode('utf-8')
        flag = xor_with_key(decoded_str, "MED")
        return flag
    except Exception as e:
        print(f"Error during final decoding or XOR: {e}")
        return None

# Encoded flag from the challenge
encoded_flag = "JJFEIRKJKJFUIS22IZKUSUZSI5EVUS2VJNKTEVCHJJDEKVKRGJDEWNKMIVCVKMSMJJFEGRSJKMZFIS2OIRKVKVCTJREVMTCVGJKTES2KJZHEKR2SKNGEWTK2IZHVEMSLJFFEWVSHKZJVISJVIZLE2USLK5FDKSKUIVKVGS2JLJDUKS2XJNJUWTSKIVLVISZSJFLEWVSJKEZEYSSGIZCVOVSKKNFVMRSWI5KEGQ2JKZGEKS2VKJJUWWSEKZCVIQ2WJM2UYRKHKNJU2SSKIVCUWU2LKNDUUTCVKNKFGR2JKZFVKNCTGJBUUTSJKZKVEQSTJNBEMRCLHU6T2"

# Solve the challenge
flag = decode_challenge(encoded_flag)
if flag:
    print("Recovered FLAG:", flag)
```

## Key Steps in the Attack

1. **Padding Adjustment**:
   - Base32 encoded strings should have a length that is a multiple of 8
   - We add padding ('=') characters if necessary to ensure proper decoding

2. **Recursive Base32 Decoding**:
   - The `decode_challenge()` function performs base32 decoding five times in succession
   - Each iteration unwraps one layer of encoding

3. **XOR Decryption**:
   - After base32 decoding, we XOR the result with the key "MED"
   - The key is applied cyclically across the entire decoded string

## Results

The script successfully recovers the flag:
```
Recovered FLAG: MED{x0r_with_m34n1ngl3ss_k3y}
```

## Why This Attack Works

This attack works because:

1. The encryption method (XOR with a fixed key) is symmetric - the same operation both encrypts and decrypts
2. The key "MED" is known and was used consistently throughout the encryption process
3. Base32 encoding is a standard encoding scheme with well-established decoding methods

## Security Implications

This challenge demonstrates why:

1. **Simple XOR encryption** is not secure for sensitive data
2. **Fixed, short keys** create patterns that can be analyzed and broken
3. **Encoding is not encryption** - base32 or other encoding schemes add no actual security

In practice, modern cryptographic applications use proper encryption algorithms with appropriate key lengths and secure modes of operation rather than simple XOR operations.

## Mathematical Foundation

The security of XOR-based encryption relies entirely on the secrecy, randomness, and length of the key. When the key is:
- Known (as in this challenge)
- Short and repeating
- Non-random (e.g., ASCII text)

The encryption offers no real security. Additionally, the base32 encoding step only obfuscates the content but doesn't add any cryptographic security.

## Flag

The recovered flag is:
```
MED{x0r_with_m34n1ngl3ss_k3y}
```

This flag suggests that using XOR with a meaningless or predictable key does not provide meaningful security - a lesson well illustrated by this challenge.