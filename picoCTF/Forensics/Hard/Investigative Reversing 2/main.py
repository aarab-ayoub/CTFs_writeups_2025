def extract_flag():
    with open('encoded.bmp', 'rb') as f:
        f.seek(2000)  # Skip BMP header
        flag_bits = []
        
        # Extract LSBs of next 400 bytes
        for _ in range(400):
            byte = ord(f.read(1))
            flag_bits.append(byte & 1)  # Get LSB
        
        flag = []
        for i in range(50):
            # Get 8 bits (in reverse order)
            bits = flag_bits[i*8 : (i+1)*8][::-1]  # Reverse for correct bit order
            
            # Convert bits to integer
            char_val = int(''.join(map(str, bits)), 2)
            
            # Reverse the (-5) adjustment
            original_char = char_val + 5
            flag.append(chr(original_char))
        
        return ''.join(flag)

# Run extraction
flag = extract_flag()
print("Flag:", flag)
