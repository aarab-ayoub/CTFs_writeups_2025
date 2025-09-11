import os
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import zlib
import base64
import hashlib
from Crypto.Random import get_random_bytes


FLAG = "MED{m3m0ry_forens1cs_1s_N0T_3asy}"  
DUMP_SIZE = 4 * 1024 * 1024  # 4MB dump

# 1. Create random dump
dump = np.random.bytes(DUMP_SIZE)

# 2. Add fake headers (ELF, PE, Mach-O)
elf_header = b"\x7fELF\x02\x01\x01" + b"\x00" * 9 + b"\x02\x00\x3e\x00"
pe_header = b"MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00"
macho_header = b"\xcf\xfa\xed\xfe\x07\x00\x00\x01"
dump = elf_header + pe_header + macho_header + dump[len(elf_header)+len(pe_header)+len(macho_header):]

# 3. Hide flag parts
# Part 1: AES-encrypted (add "AES_FLAG" header)
aes_header = b"AES_FLAG:"
key = get_random_bytes(16)  # Generate a random 16-byte AES key
cipher = AES.new(key, AES.MODE_ECB)  # Initialize AES cipher in ECB mode
encrypted_part = aes_header + cipher.encrypt(pad(FLAG[:10].encode(), AES.block_size))
dump = dump[:0x10000] + encrypted_part + dump[0x10000 + len(encrypted_part):]

# Part 2: Base64 (add "B64:" header)
b64_part = b"B64:" + base64.b64encode(FLAG[10:20].encode())
dump = dump[:0x20000] + b64_part + dump[0x20000 + len(b64_part):]

# Part 3: Zlib (keep as-is, already detectable)
zlib_part = zlib.compress(FLAG[20:].encode())
dump = dump[:0x30000] + zlib_part + dump[0x30000 + len(zlib_part):]

# 4. Save
with open("corrupted_dump_v2.bin", "wb") as f:
    f.write(dump)

print("[+] Generated 'corrupted_dump_v2.bin'")
print("[+] Flag parts hidden in AES, Base64, and Zlib segments")