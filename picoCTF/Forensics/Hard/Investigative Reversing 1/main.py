#!/usr/bin/env python3

def analyze_distribution():
    """
    Analyze the distribution pattern from the decompiled code:
    
    fread(&ptr, 0x1a, 1, iVar1);  // Read 26 bytes from flag.txt
    fputc((int32_t)ptr._1_1_, uVar4);  // ptr[1] -> mystery3.png
    fputc((int32_t)(char)((char)ptr + '\x15'), uVar3);  // ptr[0] + 0x15 -> mystery2.png
    fputc((int32_t)ptr._2_1_, uVar4);  // ptr[2] -> mystery3.png
    var_6bh._0_1_ = ptr._3_1_;  // ptr[3] -> var_6bh
    fputc((int32_t)ptr._5_1_, uVar4);  // ptr[5] -> mystery3.png
    fputc((int32_t)ptr._4_1_, iVar2);  // ptr[4] -> mystery.png
    
    // Loop: for i in range(6, 10):
    //   var_6bh += 1; fputc(ptr[i], mystery.png)  // ptr[6-9] -> mystery.png
    
    fputc((int32_t)(char)var_6bh, uVar3);  // (ptr[3] + 4) -> mystery2.png
    
    // Loop: for i in range(10, 15):
    //   fputc(ptr[i], mystery3.png)  // ptr[10-14] -> mystery3.png
    
    // Loop: for i in range(15, 26):
    //   fputc(ptr[i], mystery.png)  // ptr[15-25] -> mystery.png
    """
    
    # Extracted data from PNG files
    mystery1_data = "CF{An1_69008b75}"  # From mystery.png
    mystery2_data = bytes([0x85, 0x73])  # From mystery2.png  
    mystery3_data = "icT0tha_"  # From mystery3.png
    
    print("Distribution analysis:")
    print("mystery.png gets:  ptr[4], ptr[6-9], ptr[15-25]")
    print("mystery2.png gets: ptr[0]+0x15, ptr[3]+4")
    print("mystery3.png gets: ptr[1], ptr[2], ptr[5], ptr[10-14]")
    print()
    
    return mystery1_data, mystery2_data, mystery3_data

def recover_flag():
    mystery1_data, mystery2_data, mystery3_data = analyze_distribution()
    
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

def verify_reconstruction():
    """Verify our reconstruction logic"""
    mystery1_data = "CF{An1_69008b75}"
    mystery2_data = bytes([0x85, 0x73])
    mystery3_data = "icT0tha_"
    
    print("Verification:")
    print(f"mystery.png: {mystery1_data}")
    print(f"mystery2.png: {mystery2_data.hex()} -> {chr(mystery2_data[0])}{chr(mystery2_data[1])}")
    print(f"mystery3.png: {mystery3_data}")
    print()
    
    print("Decoded mystery2.png bytes:")
    print(f"  0x85 - 0x15 = 0x{0x85 - 0x15:02x} = '{chr(0x85 - 0x15)}'")
    print(f"  0x73 - 4 = 0x{0x73 - 4:02x} = '{chr(0x73 - 4)}'")
    print()

if __name__ == "__main__":
    verify_reconstruction()
    
    recovered_flag = recover_flag()
    print(f"Recovered flag: {recovered_flag}")
    
    # Let's also show the flag character by character
    print("\nFlag breakdown:")
    for i, char in enumerate(recovered_flag):
        print(f"  flag[{i:2d}] = '{char}'")
