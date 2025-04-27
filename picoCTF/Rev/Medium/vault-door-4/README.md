# Vault Door 4 Writeup

## Challenge Information
- **Name**: vault-door-4
- **Description**: This vault uses ASCII encoding for the password. The source code for this vault is here: VaultDoor4.java
- **Hints**: 
  - Use a search engine to find an "ASCII table".
  - You will also need to know the difference between octal, decimal, and hexadecimal numbers.

## Understanding the Challenge

Examining the provided `VaultDoor4.java` file, we can see that this challenge involves understanding different number representations and ASCII encoding. The key part of the code is the `checkPassword` method:

```java
public boolean checkPassword(String password) {
    byte[] passBytes = password.getBytes();
    byte[] myBytes = {
        106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
        0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
        0142, 0131, 0164, 063 , 0163, 0137, 0146, 064 ,
        'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ,
    };
    for (int i=0; i<32; i++) {
        if (passBytes[i] != myBytes[i]) {
            return false;
        }
    }
    return true;
}
```

The function converts our input password to a byte array and compares it with a predefined array of bytes. If they match, we have the correct password. The challenge comes from the fact that the bytes in `myBytes` are represented in different number systems.

## Solution Approach

Looking at the `myBytes` array, we can identify four different representations:

1. The first row (indices 0-7) contains decimal numbers
2. The second row (indices 8-15) uses hexadecimal notation (prefixed with `0x`)
3. The third row (indices 16-23) uses octal notation (prefixed with `0`)
4. The fourth row (indices 24-31) contains ASCII characters directly

To solve this challenge, we need to convert all these values to their ASCII character equivalents and combine them to form the password.

### Row 1: Decimal to ASCII
```
106, 85, 53, 116, 95, 52, 95, 98
```
Converting these decimal values to ASCII characters yields:
```
jU5t_4_b
```

### Row 2: Hexadecimal to ASCII
```
0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f
```
Converting these hexadecimal values to ASCII characters yields:
```
UnCh_0f_
```

### Row 3: Octal to ASCII
```
0142, 0131, 0164, 063, 0163, 0137, 0146, 064
```
Converting these octal values to ASCII characters yields:
```
bYt3s_f4
```

### Row 4: Direct ASCII
```
'a', '8', 'c', 'd', '8', 'f', '7', 'e'
```
These are already ASCII characters, so we just need to combine them:
```
a8cd8f7e
```

## The Flag

Combining all four parts and wrapping with the picoCTF flag format:
```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}
```

## Reflection

This challenge teaches us about different number systems (decimal, hexadecimal, and octal) and how they can be used to represent ASCII characters. It's a good reminder that data can be represented in multiple ways, and understanding these representations is important for many cybersecurity tasks.

In CTF challenges, it's common to see data encoded or represented in different formats to obscure information. Being comfortable with these conversions and having knowledge of ASCII tables is an essential skill.

The vault door series of challenges continues to build on concepts of reverse engineering and understanding how data is stored and manipulated in programs.
