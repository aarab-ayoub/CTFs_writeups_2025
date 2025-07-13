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
