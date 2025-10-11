# The Last Dance - Writeup

**Category:** Crypto  
**Difficulty:** Easy  
**Challenge:** The Last Dance

## Challenge Description

To be accepted into the upper class of the Berford Empire, you had to attend the annual Cha-Cha Ball at the High Court. Little did you know that among the many aristocrats invited, you would find a burned enemy spy. Your goal quickly became to capture him, which you succeeded in doing after putting something in his drink. Many hours passed in your agency's interrogation room, and you eventually learned important information about the enemy agency's secret communications. Can you use what you learned to decrypt the rest of the messages?

## Initial Analysis

We're provided with two files:

### source.py
```python
from Crypto.Cipher import ChaCha20
from secret import FLAG
import os

def encryptMessage(message, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=iv)
    ciphertext = cipher.encrypt(message)
    return ciphertext

def writeData(data):
    with open("out.txt", "w") as f:
        f.write(data)

if __name__ == "__main__":
    message = b"Our counter agencies have intercepted your messages and a lot "
    message += b"of your agent's identities have been exposed. In a matter of "
    message += b"days all of them will be captured"

    key, iv = os.urandom(32), os.urandom(12)

    encrypted_message = encryptMessage(message, key, iv)
    encrypted_flag = encryptMessage(FLAG, key, iv)

    data = iv.hex() + "\n" + encrypted_message.hex() + "\n" + encrypted_flag.hex()
    writeData(data)
```

### out.txt
```
c4a66edfe80227b4fa24d431
7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990
7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7
```

The file contains:
1. **Line 1**: Nonce (IV) - 12 bytes in hex
2. **Line 2**: Encrypted known message - 157 bytes in hex
3. **Line 3**: Encrypted flag - 51 bytes in hex

## Vulnerability Analysis

The critical vulnerability is **nonce reuse** in a stream cipher!

### How ChaCha20 Works

ChaCha20 is a **stream cipher** that generates a keystream from the key and nonce:
1. Generate keystream: `keystream = ChaCha20(key, nonce)`
2. Encrypt: `ciphertext = plaintext ⊕ keystream`
3. Decrypt: `plaintext = ciphertext ⊕ keystream`

### The Fatal Flaw

Looking at the code:
```python
key, iv = os.urandom(32), os.urandom(12)

encrypted_message = encryptMessage(message, key, iv)
encrypted_flag = encryptMessage(FLAG, key, iv)
```

**The same key and nonce are used for both encryptions!**

This means:
- `c1 = m1 ⊕ keystream`
- `c2 = m2 ⊕ keystream`

Where `c1` is the encrypted message, `c2` is the encrypted flag, and both use the **same keystream**.

### The Attack: Known-Plaintext Attack

Since we know both the plaintext (`m1`) and ciphertext (`c1`) of the first message, we can recover the keystream:

```
keystream = c1 ⊕ m1
```

Then, we can decrypt the flag:
```
flag = c2 ⊕ keystream
```

This works because:
```
c2 ⊕ keystream = (m2 ⊕ keystream) ⊕ keystream = m2
```

## Mathematical Explanation

The XOR operation has a useful property: **XOR is self-inverse**

- `A ⊕ B ⊕ B = A`

Given:
1. `c1 = m1 ⊕ ks` (known ciphertext)
2. `m1` is known (from source code)
3. `c2 = flag ⊕ ks` (flag ciphertext)

Derive keystream:
```
ks = c1 ⊕ m1
```

Recover flag:
```
flag = c2 ⊕ ks
     = c2 ⊕ (c1 ⊕ m1)
     = (flag ⊕ ks) ⊕ (c1 ⊕ m1)
     = (flag ⊕ ks) ⊕ ((m1 ⊕ ks) ⊕ m1)
     = flag ⊕ ks ⊕ m1 ⊕ ks ⊕ m1
     = flag
```

## Exploit

```python
#!/usr/bin/env python3
import binascii

# Known plaintext from source.py
known_message = (
    b"Our counter agencies have intercepted your messages and a lot "
    b"of your agent's identities have been exposed. In a matter of "
    b"days all of them will be captured"
)

def bxor(a: bytes, b: bytes) -> bytes:
    """XOR two byte strings"""
    return bytes(x ^ y for x, y in zip(a, b))

def main():
    # Read encrypted data
    with open("out.txt", "r") as f:
        iv_hex = f.readline().strip()
        c_known_hex = f.readline().strip()
        c_flag_hex = f.readline().strip()

    # Parse hex values
    iv = binascii.unhexlify(iv_hex)
    c_known = binascii.unhexlify(c_known_hex)
    c_flag = binascii.unhexlify(c_flag_hex)

    print(f"[*] IV: {iv_hex}")
    print(f"[*] Known ciphertext length: {len(c_known)} bytes")
    print(f"[*] Flag ciphertext length: {len(c_flag)} bytes")

    # Step 1: Recover keystream from known plaintext
    print("\n[*] Recovering keystream from known plaintext...")
    keystream = bxor(c_known, known_message)
    print(f"[+] Keystream recovered: {len(keystream)} bytes")

    # Step 2: Decrypt flag using recovered keystream
    print("\n[*] Decrypting flag...")
    keystream_for_flag = keystream[:len(c_flag)]
    flag = bxor(c_flag, keystream_for_flag)

    print(f"\n[+] FLAG: {flag.decode()}")

if __name__ == "__main__":
    main()
```

## Running the Exploit

```bash
$ python3 solve.py
[*] IV: c4a66edfe80227b4fa24d431
[*] Known ciphertext length: 157 bytes
[*] Flag ciphertext length: 51 bytes

[*] Recovering keystream from known plaintext...
[+] Keystream recovered: 157 bytes

[*] Decrypting flag...

[+] FLAG: HTB{und3r_th3_s34_th3r3_l1v3d_4_crypt0_m4st3r}
```

## Flag

```
HTB{und3r_th3_s34_th3r3_l1v3d_4_crypt0_m4st3r}
```

## Visual Representation

```
Known Message (m1):  "Our counter agencies have..."
                     ⊕
Ciphertext 1 (c1):   7aa34395a258f5893e3db182...
                     ↓
Keystream (ks):      [recovered bytes]
                     ⊕
Ciphertext 2 (c2):   7d8273ceb459e4d4386df4e3...
                     ↓
FLAG (m2):           "HTB{und3r_th3_s34..."
```

## Key Takeaways

1. **NEVER reuse nonces in stream ciphers** - This is catastrophic for security
2. **Stream ciphers require unique nonces per message** - Even with the same key
3. **Known-plaintext attacks are devastating with nonce reuse** - The keystream is completely exposed
4. **ChaCha20 is secure when used correctly** - The vulnerability here is implementation error, not the algorithm
5. **Two-time pad attack** - This is a variant of the classic "two-time pad" attack on stream ciphers

## Why Nonce Reuse is Critical

Stream ciphers like ChaCha20 are essentially implementing a **one-time pad** with a pseudo-random keystream. The "one-time" part is crucial:

- **One-time pad (secure)**: Each pad is used exactly once
- **Two-time pad (broken)**: Reusing a pad allows XOR relationships to reveal plaintext

When you reuse a nonce:
- You generate the **same keystream**
- Multiple messages encrypted with the same keystream can be XORed together
- This reveals `m1 ⊕ m2`, which leaks information about both messages
- With known plaintext, you can recover the entire keystream

## Proper Usage

To use ChaCha20 correctly:

```python
# CORRECT: Generate new nonce for each message
key = os.urandom(32)  # Generate once

# Message 1
nonce1 = os.urandom(12)  # New nonce
cipher1 = ChaCha20.new(key=key, nonce=nonce1)
ct1 = cipher1.encrypt(message1)

# Message 2
nonce2 = os.urandom(12)  # NEW nonce (different from nonce1)
cipher2 = ChaCha20.new(key=key, nonce=nonce2)
ct2 = cipher2.encrypt(message2)
```

## References

- [ChaCha20-Poly1305 - Wikipedia](https://en.wikipedia.org/wiki/ChaCha20-Poly1305)
- [Stream Cipher Attacks](https://en.wikipedia.org/wiki/Stream_cipher_attacks)
- [RFC 8439 - ChaCha20 and Poly1305](https://tools.ietf.org/html/rfc8439)
- [Nonce Reuse Attacks](https://en.wikipedia.org/wiki/Cryptographic_nonce)
