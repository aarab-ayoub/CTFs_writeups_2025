# Investigative Reversing 0 - PicoCTF Challenge Writeup

## Challenge Information
- **Name**: Investigative Reversing 0
- **Category**: Reverse Engineering + Forensics
- **Description**: We have recovered a binary and an image. See what you can make of it. There should be a flag somewhere.
- **Files**: 
  - Binary executable (ELF file)
  - Image file (PNG)
- **Hints**:
  1. Try using some forensics skills on the image
  2. This problem requires both forensics and reversing skills
  3. A hex editor may be helpful

## Solution Overview

This challenge combines reverse engineering and steganography. We need to analyze a binary to understand how it processes data, then apply forensics techniques to extract hidden data from an image file and reverse the transformation to recover the flag.

## Step-by-Step Solution

### Step 1: Binary Analysis - File Information
First, let's examine the binary file to understand its properties:

```bash
file mystery
```

**Output:**
```
mystery: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=34b772a4f30594e2f30ac431c72667c3e10fa3e9, not stripped
```

Check security features:
```bash
checksec mystery
```

**Output:**
```
[*] '/home/subzero/Downloads/mystery'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    Stripped:   No
```

**Key Observations:**
- 64-bit ELF executable
- **Not stripped** - symbols are available for analysis
- Standard security features enabled

### Step 2: Reverse Engineering the Binary
Since the binary is not stripped, we can decompile it using tools like Ghidra, Rizin, or IDA:

```c
void main(void)
{
    int32_t iVar1;
    int64_t iVar2;
    int64_t iVar3;
    int64_t in_FS_OFFSET;
    int c;
    int32_t var_50h;
    FILE *stream;
    FILE *var_40h;
    void *ptr;
    int64_t var_29h;
    int64_t canary;
    
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    iVar2 = fopen("flag.txt", data.00002008);
    iVar3 = fopen("mystery.png", data.00002013);
    if (iVar2 == 0) {
        puts("No flag found, please make sure this is run on the server");
    }
    if (iVar3 == 0) {
        puts("mystery.png is missing, please run this on the server");
    }
    iVar1 = fread(&ptr, 0x1a, 1, iVar2);
    if (iVar1 < 1) {
        exit(0);
    }
    puts("at insert");
    fputc((int32_t)(char)ptr, iVar3);
    fputc((int32_t)ptr._1_1_, iVar3);
    fputc((int32_t)ptr._2_1_, iVar3);
    fputc((int32_t)ptr._3_1_, iVar3);
    fputc((int32_t)ptr._4_1_, iVar3);
    fputc((int32_t)ptr._5_1_, iVar3);
    for (stack0xffffffffffffffac = 6; stack0xffffffffffffffac < 0xf; unique0x00005780 = stack0xffffffffffffffac + 1) {
        fputc((int32_t)(char)(*(char *)((int64_t)&ptr + (int64_t)stack0xffffffffffffffac) + '\x05'), iVar3);
    }
    fputc((int32_t)(char)((char)var_29h + -3), iVar3);
    for (var_50h = 0x10; var_50h < 0x1a; var_50h = var_50h + 1) {
        fputc((int32_t)*(char *)((int64_t)&ptr + (int64_t)var_50h), iVar3);
    }
    fclose(iVar3);
    fclose(iVar2);
    if (canary != *(int64_t *)(in_FS_OFFSET + 0x28)) {
        __stack_chk_fail();
    }
    return;
}
```

### Step 3: Understanding the Algorithm
Analyzing the decompiled code reveals the transformation process:

1. **File Operations**: Opens `flag.txt` and `mystery.png`
2. **Data Reading**: Reads 26 bytes (`0x1a`) from `flag.txt`
3. **Data Transformation**: Applies specific transformations to different byte ranges:
   - **Bytes 0-5**: Copied as-is
   - **Bytes 6-14**: Each byte has 5 added (`+ 0x05`)
   - **Byte 15**: Has 3 subtracted (`- 3`)
   - **Bytes 16-25**: Copied as-is
4. **Output**: Writes transformed data to `mystery.png`

### Step 4: Forensics Analysis of the Image
Use steganography tools to extract hidden data from the PNG file:

```bash
zsteg mystery.png
```

**Output:**
```
[?] 26 bytes of extra data after image end (IEND), offset = 0x1e873
extradata:0         .. 
    00000000: 70 69 63 6f 43 54 4b 80  6b 35 7a 73 69 64 36 71  |picoCTK.k5zsid6q|
    00000010: 5f 33 64 36 35 39 66 35  37 7d                    |_3d659f57}      |
imagedata           .. text: "PPP@@@@@@@@@@@@"
```

**Key Findings:**
- 26 bytes of extra data found after the PNG's IEND marker
- This represents the transformed flag data
- The data starts with "picoCTK" (likely the beginning of "picoCTF")

### Step 5: Reversing the Transformation
Create a Python script to reverse the transformation logic:

```python
# Extracted data from zsteg output
extracted_data = bytes.fromhex("70 69 63 6f 43 54 4b 80 6b 35 7a 73 69 64 36 71 5f 33 64 36 35 39 66 35 37 7d")

# Reconstruct the flag based on the binary's transformation logic
flag = bytearray()

# First 6 bytes are copied as-is
flag.extend(extracted_data[:6])

# Bytes 6-15 (9 bytes) had 5 added to each - now subtract 5
for b in extracted_data[6:15]:
    flag.append(b - 5)

# Byte 15 had 3 subtracted - now add 3
flag.append(extracted_data[15] + 3)

# Bytes 16-26 (10 bytes) are copied as-is
flag.extend(extracted_data[16:])

# Convert to string
flag_str = flag.decode('latin-1')
print(f"Recovered flag: {flag_str}")
```

### Step 6: Execute the Reversal Script
Run the Python script to recover the original flag:

```bash
python3 main.py
```

**Output:**
```
Recovered flag: picoCTF{f0und_1t_3d659f57}
```

## Key Concepts Learned

### Reverse Engineering
1. **Binary Analysis**: Using file analysis tools to understand executable properties
2. **Decompilation**: Converting machine code back to readable source code
3. **Algorithm Analysis**: Understanding data transformation logic
4. **Control Flow**: Following program execution paths

### Digital Forensics
1. **Steganography**: Hidden data embedded in image files
2. **PNG Structure**: Understanding image file formats and metadata
3. **Hex Analysis**: Working with binary data and hex representations
4. **Tool Usage**: Leveraging specialized forensic tools like zsteg

### Data Transformation
1. **Byte Manipulation**: Arithmetic operations on individual bytes
2. **Encoding/Decoding**: Reversing transformation algorithms
3. **Data Reconstruction**: Rebuilding original data from transformed versions

## Tools Used
- **file** - File type identification
- **checksec** - Security feature analysis
- **Ghidra/Rizin** - Reverse engineering and decompilation
- **zsteg** - Steganography analysis tool for PNG files
- **Python** - Script development for data transformation
- **Hex editors** - Binary data analysis

## Alternative Analysis Methods

### 1. Manual Hex Analysis
```bash
# Extract data after IEND marker
xxd mystery.png | tail -5
```

### 2. Binwalk Analysis
```bash
binwalk -e mystery.png
```

### 3. Strings Analysis
```bash
strings mystery.png | grep -i pico
```

### 4. Direct Binary Execution
```bash
# If flag.txt exists locally
echo "test_flag_here" > flag.txt
./mystery
```

## Transformation Logic Breakdown

| Byte Range | Original Operation | Reverse Operation |
|------------|-------------------|-------------------|
| 0-5        | Copy as-is        | Copy as-is        |
| 6-14       | Add 5 to each     | Subtract 5 from each |
| 15         | Subtract 3        | Add 3             |
| 16-25      | Copy as-is        | Copy as-is        |

## PNG File Structure
The challenge exploits the PNG file format by appending data after the IEND chunk:
```
[PNG Header] [IHDR] [Image Data] [IEND] [Hidden Data]
```

## Security Implications
1. **Steganography**: Data can be hidden in seemingly innocent files
2. **Binary Analysis**: Reverse engineering reveals hidden functionality
3. **Data Exfiltration**: Combining multiple techniques for covert communication
4. **Forensic Detection**: Specialized tools can detect hidden data

## Flag
```
picoCTF{f0und_1t_3d659f57}
```

## Conclusion

This challenge excellently demonstrates the intersection of reverse engineering and digital forensics. It shows how malicious software might hide data in image files using custom transformation algorithms. The solution requires both technical skills (reverse engineering, steganography) and analytical thinking (understanding the transformation logic and reversing it).

The challenge teaches important lessons about:
- Multi-disciplinary approach to cybersecurity problems
- Importance of analyzing all provided artifacts
- Understanding file formats and their exploitation potential
- Developing custom tools/scripts for specific problems

The combination of binary analysis and steganography makes this a realistic scenario that security professionals might encounter in the field.
