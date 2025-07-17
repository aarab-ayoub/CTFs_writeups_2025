# Mystery Binary Challenge Writeup

## Challenge Overview

This challenge involves reverse engineering a binary executable that distributes flag data across three PNG image files. The goal is to recover the original flag by analyzing the binary's algorithm and extracting hidden data from the images.

## Files Provided

- `mystery` - ELF 64-bit executable
- `mystery.png` - PNG image with hidden data
- `mystery2.png` - PNG image with hidden data  
- `mystery3.png` - PNG image with hidden data

## Analysis

### 1. Binary Analysis

First, let's examine the binary properties:

```bash
$ file mystery
mystery: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=1b08f7a782a77a6eeb80d7c1d621b4f16f76200a, not stripped

$ checksec mystery
[*] '/home/subzero/Downloads/mystery'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
```

The binary has modern security protections enabled but is not stripped, making reverse engineering easier.

### 2. Steganography Analysis

Using `zsteg` to analyze the PNG files for hidden data:

```bash
$ zsteg mystery.png mystery2.png mystery3.png 

[.] mystery.png
[?] 16 bytes of extra data after image end (IEND), offset = 0x1e873
extradata:0         .. text: "CF{An1_69008b75}"

[.] mystery2.png
[?] 2 bytes of extra data after image end (IEND), offset = 0x1e873
extradata:0         .. 
    00000000: 85 73                                             |.s              |

[.] mystery3.png
[?] 8 bytes of extra data after image end (IEND), offset = 0x1e873
extradata:0         .. text: "icT0tha_"
```

**Key findings:**
- `mystery.png`: Contains "CF{An1_69008b75}" (14 bytes)
- `mystery2.png`: Contains 2 bytes [0x85, 0x73]
- `mystery3.png`: Contains "icT0tha_" (8 bytes)

### 3. Reverse Engineering

Decompiling the binary reveals the main function that distributes flag data:

```c
void main(void) {
    // ... variable declarations ...
    
    iVar1 = fopen("flag.txt", "r");
    iVar2 = fopen("mystery.png", "a");
    uVar3 = fopen("mystery2.png", "a");
    uVar4 = fopen("mystery3.png", "a");
    
    fread(&ptr, 0x1a, 1, iVar1);  // Read 26 bytes from flag.txt
    
    // Distribution sequence:
    fputc((int32_t)ptr._1_1_, uVar4);                    // ptr[1] -> mystery3.png
    fputc((int32_t)(char)((char)ptr + '\x15'), uVar3);  // ptr[0] + 0x15 -> mystery2.png
    fputc((int32_t)ptr._2_1_, uVar4);                    // ptr[2] -> mystery3.png
    var_6bh._0_1_ = ptr._3_1_;                           // ptr[3] -> var_6bh
    fputc((int32_t)ptr._5_1_, uVar4);                    // ptr[5] -> mystery3.png
    fputc((int32_t)ptr._4_1_, iVar2);                    // ptr[4] -> mystery.png
    
    // Loop: ptr[6-9] -> mystery.png (var_6bh incremented each time)
    for (i = 6; i < 10; i++) {
        var_6bh._0_1_ = (char)var_6bh + '\x01';
        fputc((int32_t)*(char *)((int64_t)&ptr + (int64_t)i), iVar2);
    }
    
    fputc((int32_t)(char)var_6bh, uVar3);  // (ptr[3] + 4) -> mystery2.png
    
    // Loop: ptr[10-14] -> mystery3.png
    for (i = 10; i < 15; i++) {
        fputc((int32_t)*(char *)((int64_t)&ptr + (int64_t)i), uVar4);
    }
    
    // Loop: ptr[15-25] -> mystery.png
    for (i = 15; i < 26; i++) {
        fputc((int32_t)*(char *)((int64_t)&ptr + (int64_t)i), iVar2);
    }
    
    // ... cleanup ...
}
```

### 4. Distribution Pattern Analysis

The algorithm distributes the 26-byte flag as follows:

- **mystery.png** receives: `ptr[4], ptr[6-9], ptr[15-25]` (14 bytes total)
- **mystery2.png** receives: `ptr[0] + 0x15, ptr[3] + 4` (2 bytes total)
- **mystery3.png** receives: `ptr[1], ptr[2], ptr[5], ptr[10-14]` (8 bytes total)

## Solution

### Flag Recovery Script

```python
#!/usr/bin/env python3

def recover_flag():
    # Extracted data from PNG files
    mystery1_data = "CF{An1_69008b75}"  # From mystery.png
    mystery2_data = bytes([0x85, 0x73])  # From mystery2.png  
    mystery3_data = "icT0tha_"  # From mystery3.png
    
    # Convert to bytes
    mystery1_bytes = mystery1_data.encode('ascii')
    mystery3_bytes = mystery3_data.encode('ascii')
    
    # Initialize flag array
    flag = bytearray(26)
    
    # Reverse the distribution:
    
    # From mystery2.png:
    # First byte: ptr[0] + 0x15 = 0x85, so ptr[0] = 0x85 - 0x15 = 0x70 = 'p'
    # Second byte: ptr[3] + 4 = 0x73, so ptr[3] = 0x73 - 4 = 0x6f = 'o'
    flag[0] = mystery2_data[0] - 0x15  # 0x85 - 0x15 = 0x70 = 'p'
    flag[3] = mystery2_data[1] - 4     # 0x73 - 4 = 0x6f = 'o'
    
    # From mystery3.png: ptr[1], ptr[2], ptr[5], ptr[10-14]
    flag[1] = mystery3_bytes[0]   # 'i'
    flag[2] = mystery3_bytes[1]   # 'c'
    flag[5] = mystery3_bytes[2]   # 'T'
    flag[10] = mystery3_bytes[3]  # '0'
    flag[11] = mystery3_bytes[4]  # 't'
    flag[12] = mystery3_bytes[5]  # 'h'
    flag[13] = mystery3_bytes[6]  # 'a'
    flag[14] = mystery3_bytes[7]  # '_'
    
    # From mystery.png: ptr[4], ptr[6-9], ptr[15-25]
    mystery1_idx = 0
    flag[4] = mystery1_bytes[mystery1_idx]; mystery1_idx += 1   # 'C'
    
    for i in range(6, 10):  # ptr[6-9]
        flag[i] = mystery1_bytes[mystery1_idx]; mystery1_idx += 1
    
    for i in range(15, 26):  # ptr[15-25]
        flag[i] = mystery1_bytes[mystery1_idx]; mystery1_idx += 1
    
    return flag.decode('ascii')

if __name__ == "__main__":
    recovered_flag = recover_flag()
    print(f"Recovered flag: {recovered_flag}")
```

### Execution

```bash
$ python3 flag_recovery.py
Recovered flag: picoCTF{An0tha_1_69008b75}
```

## Flag

**`picoCTF{An0tha_1_69008b75}`**

## Key Takeaways

1. **Multi-stage Analysis**: This challenge required both steganography analysis and reverse engineering
2. **Data Transformation**: The binary didn't just split the data - it also applied mathematical transformations (adding 0x15 and incrementing by 4)
3. **Algorithm Reconstruction**: Understanding the exact sequence of operations was crucial for successful flag recovery
4. **Tool Combination**: Success required combining multiple tools: `zsteg` for steganography, decompiler for reverse engineering, and custom Python scripting for data reconstruction

## Tools Used

- `file` - File type identification
- `checksec` - Security feature analysis
- `zsteg` - Steganography detection and extraction
- Ghidra/Rizin - Binary decompilation
- Python - Custom flag recovery script
