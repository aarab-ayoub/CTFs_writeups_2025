# Investigative Reversing 2 Challenge Writeup

## Challenge Overview

**Challenge Name:** Investigative Reversing 2  
**Category:** Forensics + Reverse Engineering  
**Description:** We have recovered a binary and an image. See what you can make of it. There should be a flag somewhere.

**Hints:**
- Try using some forensics skills on the image
- This problem requires both forensics and reversing skills  
- What is LSB encoding?

This challenge combines reverse engineering and digital forensics, specifically involving LSB (Least Significant Bit) steganography in bitmap images.

## Files Provided

- `mystery` - Binary executable
- `encoded.bmp` - Bitmap image with hidden data

## Analysis

### 1. Initial Binary Execution

Running the binary reveals missing dependencies:

```bash
$ ./mystery 
No flag found, please make sure this is run on the server
original.bmp is missing, please run this on the server
[1]    6638 segmentation fault  ./mystery
```

The binary expects:
- `flag.txt` - Contains the original flag
- `original.bmp` - Source bitmap image
- Produces `encoded.bmp` - Output with embedded data

### 2. Reverse Engineering Analysis

Decompiling the binary reveals the encoding algorithm:

```c
undefined8 main(int argc, char **argv)
{
    // Variable declarations...
    
    nmemb = (FILE *)fopen("flag.txt", "r");
    stream = (FILE *)fopen("original.bmp", "r");
    var_50h = (FILE *)fopen("encoded.bmp", "w");
    
    // Error checking
    if (nmemb == (FILE *)0x0) {
        puts("No flag found, please make sure this is run on the server");
    }
    if (stream == (FILE *)0x0) {
        puts("original.bmp is missing, please run this on the server");
    }
    
    // Copy first 2000 bytes (BMP header) unchanged
    for (i = 0; i < 2000; i++) {
        fread(&ptr, 1, 1, stream);
        fputc((int32_t)(char)ptr, var_50h);
    }
    
    // Read flag (50 characters)
    var_64h = fread(&var_48h, 0x32, 1, nmemb);
    if (var_64h < 1) {
        puts("flag is not 50 chars");
        exit(0);
    }
    
    // Encode flag into image using LSB steganography
    for (var_74h._0_4_ = 0; (int32_t)var_74h < 0x32; var_74h._0_4_ = (int32_t)var_74h + 1) {
        for (var_74h._4_4_ = 0; (int32_t)var_74h._4_4_ < 8; var_74h._4_4_ = var_74h._4_4_ + 1) {
            ptr._1_1_ = codedChar((uint64_t)var_74h._4_4_, 
                                  (uint64_t)(uint32_t)(int32_t)(char)
                                  (*(char *)((int64_t)&var_48h + (int64_t)(int32_t)var_74h) + -5), 
                                  (uint64_t)(uint32_t)(int32_t)(char)ptr);
            fputc((int32_t)ptr._1_1_, var_50h);
            fread(&ptr, 1, 1, stream);
        }
    }
    
    // Copy remaining bytes unchanged
    while (ptr._2_4_ == 1) {
        fputc((int32_t)(char)ptr, var_50h);
        ptr._2_4_ = fread(&ptr, 1, 1, stream);
    }
    
    // Cleanup...
}
```

### 3. Algorithm Analysis

The encoding process:

1. **Header Preservation**: First 2000 bytes (BMP header) are copied unchanged
2. **Flag Processing**: Reads exactly 50 characters from `flag.txt`
3. **Character Transformation**: Each flag character is modified by subtracting 5 (`char - 5`)
4. **LSB Encoding**: For each transformed character:
   - Process each of the 8 bits
   - Embed each bit into the LSB of consecutive image bytes
   - Uses a `codedChar()` function to modify image bytes
5. **Remainder Copy**: Remaining image data is copied unchanged

### 4. LSB Steganography Understanding

LSB (Least Significant Bit) steganography works by:
- Replacing the least significant bit of each byte with data bits
- This creates minimal visual change (±1 in pixel values)
- 8 consecutive bytes can store 1 character (8 bits)

## Solution

### Flag Extraction Script

Based on the reverse engineering analysis, we can extract the flag:

```python
def extract_flag():
    with open('encoded.bmp', 'rb') as f:
        f.seek(2000)  # Skip BMP header (first 2000 bytes)
        flag_bits = []
        
        # Extract LSBs of next 400 bytes (50 chars × 8 bits each)
        for _ in range(400):
            byte = ord(f.read(1))
            flag_bits.append(byte & 1)  # Get LSB using bitwise AND
        
        flag = []
        # Reconstruct each character from 8 bits
        for i in range(50):
            # Get 8 bits for current character (reverse bit order)
            bits = flag_bits[i*8 : (i+1)*8][::-1]  
            
            # Convert binary string to integer
            char_val = int(''.join(map(str, bits)), 2)
            
            # Reverse the (-5) transformation applied during encoding
            original_char = char_val + 5
            flag.append(chr(original_char))
        
        return ''.join(flag)

# Execute extraction
flag = extract_flag()
print("Flag:", flag)
```

### Key Implementation Details

1. **Offset Calculation**: Skip first 2000 bytes (BMP header)
2. **Bit Extraction**: Extract LSB from each byte using `byte & 1`
3. **Bit Grouping**: Group 8 consecutive LSBs to form each character
4. **Bit Order Reversal**: Reverse bit order to match encoding sequence
5. **Character Reconstruction**: Convert 8-bit binary to ASCII value
6. **Transformation Reversal**: Add 5 to reverse the encoding subtraction

## Flag

**`[picoCTF{n3xt_0n30000000000000000000000000899f0192}]`**

## Key Takeaways

### Technical Concepts

1. **LSB Steganography**: Understanding how data is hidden in the least significant bits of image pixels
2. **Binary File Formats**: Knowledge of BMP file structure and headers
3. **Bit Manipulation**: Working with individual bits and byte operations
4. **Reverse Engineering**: Analyzing compiled code to understand algorithms

### Problem-Solving Approach

1. **Dynamic Analysis**: Running the binary to understand its behavior
2. **Static Analysis**: Decompiling to understand the encoding algorithm
3. **Algorithm Reversal**: Creating the inverse operation to extract data
4. **File Format Knowledge**: Understanding BMP structure to locate embedded data

### Tools and Techniques

- **Disassembler/Decompiler**: For reverse engineering the binary
- **Hex Editor**: For analyzing binary file structure
- **Python Scripting**: For implementing the extraction algorithm
- **Bit Operations**: Understanding binary arithmetic and manipulation

## Additional Notes

### BMP File Structure
- **File Header**: Contains file size, offset to pixel data
- **Info Header**: Contains image dimensions, color depth
- **Pixel Data**: The actual image data where steganography occurs

### LSB Encoding Advantages
- **Minimal Visual Impact**: Changes are imperceptible to human eye
- **High Capacity**: Can embed substantial amounts of data
- **Simple Implementation**: Straightforward bit manipulation

### Security Considerations
- LSB steganography is detectable with statistical analysis
- More sophisticated techniques exist for better concealment
- This challenge demonstrates basic principles in an educational context

This challenge excellently demonstrates the intersection of reverse engineering and digital forensics, showing how hidden data can be embedded in multimedia files and recovered through careful analysis.
