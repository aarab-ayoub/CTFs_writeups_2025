# BabyPacking Reverse Engineering Challenge Writeup

## Challenge Overview
This reverse engineering challenge involves an ELF 64-bit executable that uses UPX (Ultimate Packer for eXecutables) packing and includes some interesting flag encoding/decoding mechanisms.

## Initial Reconnaissance

### File Examination
```bash
$ file BabyPacking
BabyPacking: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), statically linked, no section header

$ strings BabyPacking | grep upx
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
```

### Unpacking
The first step is to unpack the executable using UPX:
```bash
$ upx -d BabyPacking -o unpacked
```

## Code Analysis

### Key Components
1. **Dummy Data**: A large 1MB array filled with 0x41 (ASCII 'A')
2. **Encoded Flag**: `8H5WbIzb1fFBfmRU9wyhX4d90VZBTV3jXM1McE0eTHeNA0y3`
3. **Fake Flag**: `TUVEe3VweF80bmRfbTByM191cHhfZjByXzN4dHI0X3A0MW59`

### Decoding Mechanism
The flag decoding process involves:
- Using a fixed seed (1337) for random number generation
- Shuffling the characters of the encoded flag
- Creating a reverse mapping to restore the original flag

### Decoding Script
```c
char *decode_flag(const char *encoded) {
    // Initialize and allocate buffers
    // Use srand(1337) to set a fixed seed
    // Create a shuffling mechanism to restore original characters
    // Return the decoded flag
}
```

## Solution Process
1. Unpack the executable using UPX
2. Analyze the decoding function
3. Apply the decoding logic to the encoded flag

### Flag Decoding
- Encoded Flag: `8H5WbIzb1fFBfmRU9wyhX4d90VZBTV3jXM1McE0eTHeNA0y3`
- Decoded Flag: `MED{upx_4nd_m0r3_upx_f0r_3xtr4_p41n}`

## Key Learnings
- UPX packing can obfuscate executable contents
- Predictable random number generation can be used for simple encoding
- Reverse engineering involves understanding the encoding/decoding logic

## Recommended Tools
- UPX for unpacking
- Reverse engineering tools like IDA, Ghidra, or radare2
- GDB for dynamic analysis

## Mitigation Recommendations
- Use more complex encoding mechanisms
- Avoid predictable random number generation
- Implement additional anti-reverse engineering techniques

## Flag
`MED{upx_4nd_m0r3_upx_f0r_3xtr4_p41n}`