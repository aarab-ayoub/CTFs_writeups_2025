from Crypto.Util.number import long_to_bytes

# Read the ciphertext
ct_hex = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
ct = bytes.fromhex(ct_hex)

# Decryption: m = (c - 18) * inv(123, 256) mod 256
# Find modular inverse of 123 mod 256
a_inv = pow(123, -1, 256)

print(f"Modular inverse of 123 mod 256: {a_inv}")

# Decrypt each byte
msg = []
for byte in ct:
    m = ((byte - 18) * a_inv) % 256
    msg.append(m)

flag = bytes(msg)
print(f"\n[+] FLAG: {flag.decode()}")
