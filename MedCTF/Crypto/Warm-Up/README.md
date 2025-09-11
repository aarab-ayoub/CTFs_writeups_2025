# RSA Cube Root Attack With CRT Writeup

## Challenge Overview

This cryptography challenge involves exploiting a weakness in RSA encryption when the same message is encrypted using three different moduli but with the same small public exponent (e=3).

## Key Vulnerability: Same Message, Multiple Moduli

In this challenge, the same ciphertext appears three times:
```python
c1 = c2 = c3 = 12017081822503546073431493884665593178539019181337674636244195960049836053175723518596881154793179960305499522741115411263338337250807367923645690238458597674165826835130566619393939565324432341007562650266817277540767002947460586947445042500453
```

This is encrypted under three different moduli:
```python
n1 = 104720634050182887542906195819174344372480779583650899487645324350059848317489763409111604167360982570807270618313992279667858410603545755929630389443950609964301928532628474751986308753518404117721195764019925195400138254671260901386511928414770467531035961652797108979928920762898150131162852748226789491877

n2 = 77054150279575683994136666749403701562138921365779550008440254446100524319679058579426468142459778545260014200122214428836774659448547446411341137850504853240949823271574659924994974884501274912950133546912607495003269631400129417779972856841959859353656874053399543294751247378189068004181387083002510915591

n3 = 88562207105942063794522023461757235524545262559306604248912551397405812221580296268217103652532500666438725564742530414857064026713082244085062200886775953231506086165496248248270599180241501849506721285233487646808614584103955878474226944021787264611828112844405361669414355663480810900725194554746656933143
```

This configuration is vulnerable to a classic RSA attack known as the **Håstad's Broadcast Attack**.

## Theoretical Background

In RSA encryption with public exponent e, a message m is encrypted as:
```
c ≡ m^e (mod n)
```

When the same message m is encrypted with the same exponent e under different moduli, and e is small (typically 3), then there's a vulnerability.

With e = 3 and three different moduli, we have:
```
c1 ≡ m^3 (mod n1)
c2 ≡ m^3 (mod n2)
c3 ≡ m^3 (mod n3)
```

If the moduli are relatively prime (which is almost certainly true for randomly generated RSA moduli), we can use the Chinese Remainder Theorem (CRT) to find m^3 in the much larger modulus N = n1 × n2 × n3.

If m^3 < N, then the modular congruence becomes an exact equality:
```
m^3 = CRT solution
```

We can then simply take the cube root of the CRT solution to recover m.

## Attack Implementation

The attack is implemented in the provided script:

```python
from Crypto.Util.number import long_to_bytes, inverse
from sympy import integer_nthroot

# Given values from the challenge
n1 = 104720634050182887542906195819174344372480779583650899487645324350059848317489763409111604167360982570807270618313992279667858410603545755929630389443950609964301928532628474751986308753518404117721195764019925195400138254671260901386511928414770467531035961652797108979928920762898150131162852748226789491877
c1 = 12017081822503546073431493884665593178539019181337674636244195960049836053175723518596881154793179960305499522741115411263338337250807367923645690238458597674165826835130566619393939565324432341007562650266817277540767002947460586947445042500453
n2 = 77054150279575683994136666749403701562138921365779550008440254446100524319679058579426468142459778545260014200122214428836774659448547446411341137850504853240949823271574659924994974884501274912950133546912607495003269631400129417779972856841959859353656874053399543294751247378189068004181387083002510915591
c2 = 12017081822503546073431493884665593178539019181337674636244195960049836053175723518596881154793179960305499522741115411263338337250807367923645690238458597674165826835130566619393939565324432341007562650266817277540767002947460586947445042500453
n3 = 88562207105942063794522023461757235524545262559306604248912551397405812221580296268217103652532500666438725564742530414857064026713082244085062200886775953231506086165496248248270599180241501849506721285233487646808614584103955878474226944021787264611828112844405361669414355663480810900725194554746656933143
c3 = 12017081822503546073431493884665593178539019181337674636244195960049836053175723518596881154793179960305499522741115411263338337250807367923645690238458597674165826835130566619393939565324432341007562650266817277540767002947460586947445042500453

def crt(c_list, n_list):
    N = n_list[0] * n_list[1] * n_list[2]
    result = 0
    for i in range(3):
        ni = n_list[i]
        ai = c_list[i]
        Ni = N // ni
        mi = inverse(Ni, ni)
        result += ai * mi * Ni
    return result % N

# Apply Chinese Remainder Theorem
c = crt([c1, c2, c3], [n1, n2, n3])

# Take the cube root
m, exact = integer_nthroot(c, 3)
if exact:
    flag = long_to_bytes(m)
    print("Recovered FLAG:", flag)
else:
    print("Failed to recover exact root.")
```

## Key Steps in the Attack

1. **Chinese Remainder Theorem (CRT)**: 
   - The `crt()` function combines the three congruence equations into a single equation modulo N = n1 × n2 × n3
   - For each modulus ni, we calculate Ni = N/ni and its modular multiplicative inverse mi
   - The CRT solution is the sum of ai × mi × Ni for each triplet (ai, mi, Ni)

2. **Integer Cube Root**:
   - Once we have c ≡ m^3 (mod N), we need to find m
   - Since N is very large (product of three RSA moduli), if m^3 < N, then c = m^3 exactly
   - The `integer_nthroot()` function from sympy computes the integer cube root of c

3. **Conversion to Bytes**:
   - The recovered integer m is converted to bytes using `long_to_bytes()`
   - This reveals the original message/flag

## Results

The script successfully recovers the flag:
```
Recovered FLAG: b'MED{r5a_3ncrypt10n_r0cks_f0r_3v3r}'
```

## Why This Attack Works

This attack works because:

1. The same message was encrypted with the same small exponent (e=3) under three different moduli
2. With three samples and e=3, we have exactly enough equations to solve for m
3. The value of m^3 is smaller than the product of the three moduli (N)

## Security Implications

This challenge demonstrates why:

1. **Using a small public exponent** (like e=3) can be risky if not implemented properly
2. **Padding schemes** should be used when encrypting with RSA
3. **Randomization** should be part of any encryption scheme

In practice, modern RSA implementations use proper padding schemes (like PKCS#1 v1.5 or OAEP) which add randomness to the plaintext before encryption, preventing this type of attack even with small exponents.

## Mathematical Foundation

The Chinese Remainder Theorem states that if m1, m2, m3 are pairwise coprime positive integers, then the system of congruences:
```
x ≡ a1 (mod m1)
x ≡ a2 (mod m2)
x ≡ a3 (mod m3)
```

has a unique solution modulo M = m1 × m2 × m3.

In our case, we have:
```
m^3 ≡ c1 (mod n1)
m^3 ≡ c2 (mod n2)
m^3 ≡ c3 (mod n3)
```

And we're solving for m^3, which gives us m after taking the cube root.

## Flag

The recovered flag is:
```
MED{r5a_3ncrypt10n_r0cks_f0r_3v3r}
```

Which ironically celebrates RSA encryption despite demonstrating one of its vulnerabilities when improperly implemented.