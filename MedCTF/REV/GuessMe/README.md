# GuessMe Advanced Reverse Engineering Challenge Writeup

## Challenge Overview

This reverse engineering challenge involves a binary with extreme obfuscation techniques, designed to test advanced analysis skills:

* **Massive Function Obfuscation**: Over 50,000 junk functions
* **Critical Function Identification**: Hidden flag decoding mechanism in a specifically numbered function (`junk_func_1337`)
* **Complex Multi-layer Encryption**: Requiring several decoding steps

## Binary Characteristics

### Function Analysis
* Total of approximately 50,000 junk functions
* Deliberately created to overwhelm analysis tools and discourage manual inspection
* Key insight: CTF challenge name hints at function number 1337 (leet) being significant

### Key Discoveries
* Memory location `0x8ee040` contains the encoded flag data (identified via `info variables` command)
* The specific function `junk_func_1337` implements the flag decoding mechanism
* Function naming convention intentionally leverages CTF culture (1337 = "leet")

## Technical Analysis

### Memory Inspection
```
pwndbg> info variables 
All defined variables:
[...]
0x00000000008ee040  ait_lflag
[...]

pwndbg> x/128bx 0x00000000008ee040
0x8ee040:   0x0f    0x13    0x6c    0x68    0x02    0x1d    0x1c    0x0d
0x8ee048:   0x1e    0x19    0x02    0x68    0x02    0x1d    0x1c    0x0d
[...]
```

### Disassembly Insights
The disassembly of `junk_func_1337` reveals a sophisticated two-step decoding process:

1. **XOR Operation**
   * Uses a fixed XOR key (0x5A) at instruction `<+149>-<+153>`
   ```assembly
   0x0000000000031199 <+149>:   movzx  eax,BYTE PTR [rbp-0x31]
   0x000000000003119d <+153>:   xor    edx,eax
   ```

2. **Rotation Technique**
   * Rotates bytes by 3 positions in the second loop `<+263>-<+321>`
   ```assembly
   0x000000000003120d <+265>:   mov    eax,DWORD PTR [rbp-0x38]  ; rotation value (3)
   [...]
   0x0000000000031223 <+287>:   mov    rax,QWORD PTR [rbp-0x48]
   0x0000000000031227 <+291>:   movzx  eax,BYTE PTR [rax+rdx*1]
   ```

## Decoding Implementation

```python
def reverse_flag(hex_output):
    # Convert hex to bytes
    hex_bytes = bytes.fromhex(hex_output)
    
    # Rotate bytes (3 positions)
    rot = 3
    rotated = hex_bytes[-rot:] + hex_bytes[:-rot]
    
    # XOR with key 0x5A
    xor_key = 0x5A
    original_bytes = bytes([b ^ xor_key for b in rotated])
    
    return original_bytes.decode('ascii')

# Extracted hex bytes from memory location 0x8ee040
hex_output = "0f 13 6c 68 02 1d 1c 0d 1e 19 02 68 02 1d 1c 0d 1e 19 02 00 0e 14 08 0b 0c 6c 0e 1e 16 14 18 69 0d 09 69 0e 10 0a 10 0a 0f 03 15 16 18 16 6f 1e 1d 03 14 1e 12 0a 0f 67 67 67 67 67 67 10 0c 19"
hex_output = hex_output.replace(" ", "")
flag = reverse_flag(hex_output)
print("Recovered flag:", flag)
```

## Complete Solution Path

1. **Binary Analysis**
   * Initial enumeration revealing the extreme number of functions (50,000+)
   * Recognition of CTF pattern indicating significance of function 1337

2. **Memory Analysis**
   * Located the encoded flag data at `0x8ee040` (ait_lflag)
   * Extracted the raw hex bytes 

3. **Algorithm Reverse Engineering**
   * Disassembled the `junk_func_1337` function
   * Identified the two key operations:
     * XOR with key 0x5A
     * Rotation by 3 bytes

4. **Multi-stage Decoding**
   * Applied Python script to perform initial decoding:
     ```
     Recovered intermediate flag: 
     JVCUI62XGFWDCX2XGFWDCXZTNRQV6TDLNB3WS3TJPJPUYOLBL5DGYNDHPU======
     ```
   * Recognized Base32 encoding pattern (characters + padding)
   * Applied Base32 decoding:
     ```bash
     $ echo JVCUI62XGFWDCX2XGFWDCXZTNRQV6TDLNB3WS3TJPJPUYOLBL5DGYNDHPU====== | base32 -d
     MED{W1l1_W1l1_3la_Lkhwiniz_L9a_Fl4g}
     ```

## Advanced Obfuscation Techniques Observed

1. **Function Flooding**: The extreme number of junk functions (50,000+) is designed to:
   * Overload disassemblers and decompilers
   * Make manual analysis extremely time-consuming
   * Hide the critical function among thousands of irrelevant ones

2. **Cultural Obfuscation**: Using the function name `junk_func_1337` as a hint that would only be recognized by someone familiar with CTF conventions

3. **Multi-layer Encryption**: Combining multiple simple techniques (XOR, rotation, Base32) to create a more complex encoding scheme

## Flag Extraction

Final Flag: `MED{W1l1_W1l1_3la_Lkhwiniz_L9a_Fl4g}`

## Lessons & Techniques

* **Pattern Recognition**: Noticing the significance of "1337" in the function naming
* **Targeted Analysis**: Focusing on specific functions rather than getting overwhelmed by the sheer number
* **Memory Inspection**: Examining key memory locations identified through variable analysis
* **Multi-stage Decoding**: Recognizing that complex challenges often involve multiple layers of encoding/encryption
* **Tool Proficiency**: Effective use of GDB/pwndbg for memory examination and disassembly

## Conclusion

This challenge demonstrates advanced binary obfuscation techniques and reinforces the importance of focusing on patterns and specific indicators rather than attempting exhaustive analysis of heavily obfuscated binaries. The use of massive function flooding (50,000+ functions) represents an extreme case of obfuscation rarely seen in typical CTF challenges.