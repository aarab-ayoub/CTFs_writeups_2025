with open("corrupted_dump.bin", "rb") as f:
    data = f.read()
xor_key = 0xAA
decrypted = bytes([b ^ xor_key for b in data[0x10000:0x10000+30]])
print(decrypted)  # MED{m3m0ry_forens1cs_1s_fun}