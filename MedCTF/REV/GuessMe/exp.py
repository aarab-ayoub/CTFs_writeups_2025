import base64

def reverse_flag(hex_output):
    hex_bytes = bytes.fromhex(hex_output)
    
    rot = 3
    rotated = hex_bytes[-rot:] + hex_bytes[:-rot]
    
    xor_key = 0x5A
    original_bytes = bytes([b ^ xor_key for b in rotated])
    
    return original_bytes.decode('ascii')

hex_output = "0f 13 6c 68 02 1d 1c 0d 1e 19 02 68 02 1d 1c 0d 1e 19 02 00 0e 14 08 0b 0c 6c 0e 1e 16 14 18 69 0d 09 69 0e 10 0a 10 0a 0f 03 15 16 18 16 6f 1e 1d 03 14 1e 12 0a 0f 67 67 67 67 67 67 10 0c 19"

hex_output = hex_output.replace(" ", "")

flag = reverse_flag(hex_output)

decoded_flag = base64.b32decode(flag.encode()) 
print("Recovered flag:", decoded_flag.decode('ascii')) 