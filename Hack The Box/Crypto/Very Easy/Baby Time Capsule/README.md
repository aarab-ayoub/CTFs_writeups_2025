# Baby Time Capsule - Writeup

**Category:** Crypto  
**Difficulty:** Very Easy  
**Challenge:** Baby Time Capsule

## Challenge Description

Qubit Enterprises is a new company touting it's propriety method of qubit stabilization. They expect to be able to build a quantum computer that can factor a RSA-1024 number in the next 10 years. As a promotion they are giving out "time capsules" which contain a message for the future encrypted by 1024 bit RSA. They might be great engineers, but they certainly aren't cryptographers, can you find a way to read the message without having to wait for their futuristic machine?

## Initial Analysis

We're provided with a server that offers "time capsules" - RSA encrypted messages. Connecting to the server and requesting a capsule gives us:

```json
{
  "time_capsule": "39CC3231E71CD58171ABC537600CDF26AF6F072BA5ACEE4D2D54A542F91323F6...",
  "pubkey": ["ACFFE4EB687B49ABF59162862B206E90290C1337BC16FECD3575EDC00D1E8695...", "5"]
}
```

The response contains:
- `time_capsule`: The ciphertext (c) in hexadecimal
- `pubkey`: An array with the RSA modulus (n) and public exponent (e)

## Source Code Analysis

Looking at the provided `server.py`:

```python
class TimeCapsule():
    def __init__(self, msg):
        self.msg = msg
        self.bit_size = 1024
        self.e = 5  # Small public exponent!
```

Key observations:
1. **Same message encrypted multiple times**: The FLAG is encrypted with different RSA keys each time we request a capsule
2. **Small public exponent**: e = 5 (very small!)
3. **Different moduli**: Each capsule uses a freshly generated n = p × q
4. **No padding**: Raw RSA encryption with no padding scheme

This is a textbook setup for **Håstad's Broadcast Attack**.

## Vulnerability: Håstad's Broadcast Attack

When the same message `m` is encrypted with the same small exponent `e` but different moduli, we can recover the plaintext without factoring any of the moduli.

### The Math

If we collect `e` encryptions (in this case, 5):
- c₁ ≡ m⁵ (mod n₁)
- c₂ ≡ m⁵ (mod n₂)
- c₃ ≡ m⁵ (mod n₃)
- c₄ ≡ m⁵ (mod n₄)
- c₅ ≡ m⁵ (mod n₅)

Using the **Chinese Remainder Theorem (CRT)**, we can combine these into:
- m⁵ ≡ C (mod n₁ × n₂ × n₃ × n₄ × n₅)

Since the flag is relatively small (much smaller than even a single 1024-bit modulus), we have:
- m⁵ < n₁ × n₂ × n₃ × n₄ × n₅

This means `C = m⁵` over the integers, not just modulo the product. Therefore, we can simply compute the **integer 5th root** of C to recover m!

## Exploit

### Step 1: Collect Multiple Encryptions

Connect to the server 5 times and collect the ciphertext and modulus pairs:

```python
def get_time_capsule(host, port):
    conn = remote(host, port)
    conn.recvuntil(b'(Y/n) ')
    conn.sendline(b'Y')
    response = conn.recvline().decode().strip()
    conn.close()
    
    data = json.loads(response)
    c = int(data['time_capsule'], 16)
    n = int(data['pubkey'][0], 16)
    e = int(data['pubkey'][1], 16)
    
    return c, n, e
```

### Step 2: Apply Chinese Remainder Theorem

Combine the 5 congruences into one:

```python
def crt(remainders, moduli):
    total = 0
    prod = 1
    for m in moduli:
        prod *= m
    
    for r, m in zip(remainders, moduli):
        p = prod // m
        total += r * pow(p, -1, m) * p
    
    return total % prod
```

### Step 3: Compute Integer 5th Root

Extract the plaintext by taking the 5th root:

```python
def integer_nth_root(n, k):
    if n == 0:
        return 0
    if k == 1:
        return n
    
    x = n
    while True:
        x_new = ((k - 1) * x + n // (x ** (k - 1))) // k
        if x_new >= x:
            return x
        x = x_new
```

### Step 4: Convert to Flag

```python
flag = long_to_bytes(m)
print(f"[+] FLAG: {flag.decode()}")
```

## Full Exploit Code

```python
#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import long_to_bytes
import json

def integer_nth_root(n, k):
    """Compute the integer k-th root of n using Newton's method"""
    if n == 0:
        return 0
    if k == 1:
        return n
    
    x = n
    while True:
        x_new = ((k - 1) * x + n // (x ** (k - 1))) // k
        if x_new >= x:
            return x
        x = x_new

def crt(remainders, moduli):
    """Chinese Remainder Theorem"""
    total = 0
    prod = 1
    for m in moduli:
        prod *= m
    
    for r, m in zip(remainders, moduli):
        p = prod // m
        total += r * pow(p, -1, m) * p
    
    return total % prod

def get_time_capsule(host, port):
    """Connect to server and get one time capsule"""
    conn = remote(host, port)
    conn.recvuntil(b'(Y/n) ')
    conn.sendline(b'Y')
    response = conn.recvline().decode().strip()
    conn.close()
    
    data = json.loads(response)
    c = int(data['time_capsule'], 16)
    n = int(data['pubkey'][0], 16)
    e = int(data['pubkey'][1], 16)
    
    return c, n, e

def main():
    host = '94.237.123.119'
    port = 47099
    
    print("[*] Collecting time capsules...")
    
    ciphertexts = []
    moduli = []
    e = 5
    
    for i in range(e):
        print(f"[*] Getting capsule {i+1}/{e}...")
        c, n, _ = get_time_capsule(host, port)
        ciphertexts.append(c)
        moduli.append(n)
    
    print("\n[*] Applying Chinese Remainder Theorem...")
    m_to_e = crt(ciphertexts, moduli)
    
    print("[*] Computing 5th root...")
    m = integer_nth_root(m_to_e, e)
    
    print("[*] Converting to bytes...")
    flag = long_to_bytes(m)
    
    print(f"\n[+] FLAG: {flag.decode()}")

if __name__ == '__main__':
    main()
```

## Running the Exploit

```bash
$ python3 exploit.py
[*] Collecting time capsules...
[*] Getting capsule 1/5...
[*] Getting capsule 2/5...
[*] Getting capsule 3/5...
[*] Getting capsule 4/5...
[*] Getting capsule 5/5...

[*] Applying Chinese Remainder Theorem...
[*] Computing 5th root...
[*] Converting to bytes...

[+] FLAG: HTB{...}
```

## Flag

```
HTB{...}
```

## Key Takeaways

1. **Never use small public exponents with textbook RSA** - Always use proper padding (like OAEP)
2. **Never encrypt the same message multiple times** with related keys - This is exactly what broadcast attacks exploit
3. **Low exponent attacks are powerful** - With e=3, you only need 3 encryptions. With e=5, you need 5
4. **CRT is a powerful tool** - It allows combining multiple modular equations into one

## References

- [Håstad's Broadcast Attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack#H%C3%A5stad's_broadcast_attack)
- [RSA (cryptosystem) - Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
