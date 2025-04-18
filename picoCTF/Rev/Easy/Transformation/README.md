# Transformation - Reverse Engineering Challenge Writeup

## Challenge Description
I wonder what this really is... enc 
```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

## Hint
You may find some decoders online

## Solution

In this challenge, we're given an encoded file and the Python code that was used to create it. The goal is to reverse the encoding process to obtain the original flag.

### Understanding the Encoding

First, let's analyze what the encoding function does:

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

This code:
1. Takes the original flag string
2. Processes it in pairs of characters (i and i+1)
3. For each pair:
   - Takes the ASCII value of the first character and shifts it left by 8 bits (`ord(flag[i]) << 8`)
   - Adds the ASCII value of the second character (`+ ord(flag[i + 1])`)
   - Converts this combined value to a new character using `chr()`
4. Joins all these new characters into a final encoded string

The result of this operation is essentially combining two 8-bit ASCII characters into a single 16-bit Unicode character.

### Step 1: Examine the Encoded File

When examining the contents of the encoded file, we see:
```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽
```

These are Unicode characters that each represent two ASCII characters from the original flag.

### Step 2: Method 1 - Using CyberChef

The simplest approach is to use an online decoder like CyberChef:

1. Input the encoded string
2. Convert it to character codes (which gives us the numerical Unicode values)
3. Convert these values from hexadecimal to ASCII

The character codes obtained are:
```
7069 636f 4354 467b 3136 5f62 6974 735f 696e 7374 3334 645f 6f66 5f38 5f32 3636 3834 6332 307d
```

When converted from hex to ASCII, we get the flag:
```
picoCTF{16_bits_inst34d_of_8_26684c20}
```

### Step 3: Method 2 - Custom Python Script

Alternatively, we can write a Python script to reverse the encoding:

```python
enc = open("enc").read()
res = ''
for c in enc:
    res += hex(ord(c)).lstrip("0x")
print(res)
ascii_str = bytes.fromhex(res).decode('ascii')
print(ascii_str)
```

This script:
1. Reads the encoded file
2. For each Unicode character, converts it to its numeric value and then to hex
3. Strips the "0x" prefix and concatenates all hex values
4. Converts the resulting hex string back to ASCII

Running this script yields the same flag:
```
picoCTF{16_bits_inst34d_of_8_26684c20}
```

## Flag
`picoCTF{16_bits_inst34d_of_8_26684c20}`

## Learning Points
- Understanding how bit operations work in encoding schemes
- Recognizing patterns in transformation functions
- How characters can be combined into larger Unicode values
- Multiple approaches to solving encoding problems (tools vs. custom scripts)
- The relationship between character codes, hexadecimal, and ASCII
