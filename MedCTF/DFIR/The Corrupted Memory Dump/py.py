import os
import numpy as np

FLAG = "MED{m3m0ry_15_4_5c13n7ific_4r7f4c7}"  
FAKE_FLAGS = [
    "MED{r34lly_7h47_f457_u_4r3_1n54n3_bu7_17_f4k3_fl4g}",
    "MED{1_4m_4_f4k3_fl4g_4nd_1_4m_0nly_h3r3_f0r_y0u}",
    "MED{175_f4k3_4l50_4jm3}"
]
DUMP_SIZE = 2 * 1024 * 1024

dump = np.random.bytes(DUMP_SIZE)

elf_header = (
    b"\x7fELF\x02\x01\x01" + b"\x00" * 9 + 
    b"\x02\x00" + b"\x3e\x00" + b"\x01\x00\x00\x00"
)
dump = elf_header + dump[len(elf_header):]

# 3. Insert fake flags with unique XOR keys
fake_flag_offsets = []
for fake_flag in FAKE_FLAGS:
    xor_key_fake = np.random.randint(1, 256)
    fake_offset = np.random.randint(0x1000, 0x10000)  
    encrypted_fake_flag = bytes([ord(c) ^ xor_key_fake for c in fake_flag])
    dump = dump[:fake_offset] + encrypted_fake_flag + dump[fake_offset + len(encrypted_fake_flag):]
    fake_flag_offsets.append((fake_offset, xor_key_fake))

# 4. Insert the real flag after all fake flags
heap_start = 0x10000
xor_key_real = 0xAA
encrypted_flag = bytes([ord(c) ^ xor_key_real for c in FLAG])
dump = dump[:heap_start] + encrypted_flag + dump[heap_start + len(encrypted_flag):]

with open("corrupted_dump.bin", "wb") as f:
    f.write(dump)

print("[+] Generated 'corrupted_dump.bin'")
print(f"[+] Real flag hidden at offset 0x{heap_start:04x} (XOR key: 0x{xor_key_real:02x})")
for i, (offset, key) in enumerate(fake_flag_offsets):
    print(f"[+] Fake flag {i+1} hidden at offset 0x{offset:04x} (XOR key: 0x{key:02x})")