encrypted_bytes = bytes.fromhex("41 3a 34 40 72 25 75 4c 34 46 66 30 66 39 62 30 33 3d 5f 63 66 30 62 65 35 35 62 60 65 32 4e")
decrypted = []

for byte in encrypted_bytes:
    if byte > 0x20 and byte != 0x7F:  # Same conditions as in the original function
        # Reverse the transformation (subtract 47, wrap around modulo 94)
        decrypted_byte = byte - 0x2F
        if decrypted_byte < 0x20:  # If subtraction goes below 0x20, wrap around
            decrypted_byte += 0x5E
        decrypted.append(decrypted_byte)
    else:
        decrypted.append(byte)  # Leave spaces and DEL unchanged

# Convert back to a string
flag = bytes(decrypted).decode('ascii')
print(f"Decrypted flag: {flag}")
