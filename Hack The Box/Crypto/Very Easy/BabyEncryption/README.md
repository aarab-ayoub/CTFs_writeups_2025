# BabyEncryption - Writeup

**Category:** Crypto  
**Difficulty:** Very Easy  
**Challenge:** BabyEncryption

## Challenge Description

You are after an organised crime group which is responsible for the illegal weapon market in your country. As a secret agent, you have infiltrated the group enough to be included in meetings with clients. During the last negotiation, you found one of the confidential messages for the customer. It contains crucial information about the delivery. Do you think you can decrypt it?

## Initial Analysis

We're provided with two files:

### chall.py
```python
import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
```

### msg.enc
```
6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921
```

## Vulnerability Analysis

The encryption function implements a simple **affine cipher** applied byte-by-byte:

```
c = (123 * m + 18) mod 256
```

Where:
- `c` = ciphertext byte
- `m` = plaintext byte
- `123` = multiplicative constant (a)
- `18` = additive constant (b)
- `256` = modulus

This is a classic **affine transformation** and is completely reversible as long as the multiplicative constant is coprime with the modulus (gcd(123, 256) must equal 1).

### Why is this insecure?

1. **Deterministic** - Same plaintext byte always maps to same ciphertext byte
2. **No key** - The constants are hardcoded and visible in the source
3. **Byte-by-byte** - Each byte is encrypted independently (ECB-like behavior)
4. **Simple mathematics** - Easily reversible with basic modular arithmetic

## Mathematical Solution

To decrypt, we need to invert the affine transformation:

Starting with: `c ≡ 123m + 18 (mod 256)`

Solve for m:
1. Subtract 18: `c - 18 ≡ 123m (mod 256)`
2. Multiply by multiplicative inverse: `m ≡ (c - 18) × 123⁻¹ (mod 256)`

We need to find `123⁻¹ mod 256` (the modular inverse of 123 modulo 256).

### Finding the Modular Inverse

The modular inverse of 123 mod 256 is the value `x` such that:
```
123 × x ≡ 1 (mod 256)
```

We can verify: `123 × 179 = 22017 = 86 × 256 + 1`, so `123 × 179 ≡ 1 (mod 256)`

Therefore: **123⁻¹ ≡ 179 (mod 256)**

### Decryption Formula

```
m = (c - 18) × 179 mod 256
```

## Exploit

```python
#!/usr/bin/env python3

def decrypt_affine(ct_hex):
    """Decrypt affine cipher with parameters a=123, b=18, mod=256"""
    
    # Parse ciphertext
    ct = bytes.fromhex(ct_hex)
    
    # Find modular inverse of 123 mod 256
    # 123 * 179 ≡ 1 (mod 256)
    a_inv = pow(123, -1, 256)
    print(f"[*] Modular inverse of 123 mod 256: {a_inv}")
    
    # Decrypt: m = (c - 18) * a_inv mod 256
    plaintext = []
    for byte in ct:
        m = ((byte - 18) * a_inv) % 256
        plaintext.append(m)
    
    return bytes(plaintext)

def main():
    # Ciphertext from msg.enc
    ct_hex = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
    
    print("[*] Decrypting affine cipher...")
    plaintext = decrypt_affine(ct_hex)
    
    print(f"[+] Decrypted message: {plaintext.decode()}")

if __name__ == '__main__':
    main()
```

## Running the Exploit

```bash
$ python3 solve.py
[*] Modular inverse of 123 mod 256: 179
[*] Decrypting affine cipher...
[+] Decrypted message: HTB{...}
```

## Alternative: Brute Force Approach

Since there are only 256 possible values for each constant, we could also brute force:

```python
ct = bytes.fromhex(ct_hex)

# Try all possible multiplicative inverses
for a_inv in range(256):
    try:
        # Check if this could be valid
        msg = bytes([((byte - 18) * a_inv) % 256 for byte in ct])
        if b'HTB{' in msg:
            print(f"Found with a_inv={a_inv}: {msg.decode()}")
            break
    except:
        pass
```

## Flag

```
HTB{...}
```

## Key Takeaways

1. **Affine ciphers are not secure** - They're educational tools, not meant for real encryption
2. **ECB-like behavior is dangerous** - Encrypting bytes independently reveals patterns
3. **Modular arithmetic is reversible** - If gcd(a, m) = 1, we can always find the inverse
4. **Never roll your own crypto** - Use established, peer-reviewed encryption algorithms
5. **Key visibility** - Having the encryption algorithm visible makes attacks trivial

## Mathematical Background

### Affine Cipher

The affine cipher is a type of monoalphabetic substitution cipher where each character is mapped via:
```
E(x) = (ax + b) mod m
```

Decryption requires:
```
D(x) = a⁻¹(x - b) mod m
```

Where `a⁻¹` is the modular multiplicative inverse of `a` modulo `m`.

### Requirements

For the affine cipher to work:
- `gcd(a, m) = 1` (a must be coprime with m)
- Otherwise, the transformation is not bijective and cannot be reversed

In our case:
- `gcd(123, 256) = 1` ✓ (since 123 is odd and 256 is a power of 2)

## References

- [Affine Cipher - Wikipedia](https://en.wikipedia.org/wiki/Affine_cipher)
- [Modular Multiplicative Inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)
- [Extended Euclidean Algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
