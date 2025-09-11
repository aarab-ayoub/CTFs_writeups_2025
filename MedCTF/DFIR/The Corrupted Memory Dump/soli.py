with open("corrupted_dump.bin", "rb") as f:
    data = f.read()

found_flags = []

for key in range(256):
    decoded = bytes([b ^ key for b in data])
    if b"MED{" in decoded:
        # Extract all occurrences of "MED{" in the decoded data
        flags = decoded.decode(errors="ignore").split("MED{")
        for flag in flags[1:]:
            flag = "MED{" + flag.split("}")[0] + "}"
            if flag not in found_flags:
                found_flags.append((key, flag))
                print(f"Found potential flag with key {key}: {flag}")

print("\n[+] All potential flags found:")
for key, flag in found_flags:
    print(f"Key: {key}, Flag: {flag}")

