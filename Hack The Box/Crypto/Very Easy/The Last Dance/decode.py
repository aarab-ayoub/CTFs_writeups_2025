#!/usr/bin/env python3
# recover_flag.py
import binascii

# the known plaintext from the challenge (must match exactly)
known_message = (
    b"Our counter agencies have intercepted your messages and a lot "
    b"of your agent's identities have been exposed. In a matter of "
    b"days all of them will be captured"
)

def bxor(a: bytes, b: bytes) -> bytes:
    # XOR two byte-strings up to the shorter length
    return bytes(x ^ y for x, y in zip(a, b))

def main():
    with open("out.txt", "r") as f:
        iv_hex = f.readline().strip()
        c_known_hex = f.readline().strip()
        c_flag_hex = f.readline().strip()

    iv = binascii.unhexlify(iv_hex)            # not strictly needed for XOR attack
    c_known = binascii.unhexlify(c_known_hex)
    c_flag = binascii.unhexlify(c_flag_hex)

    # derive keystream bytes from known plaintext
    ks = bxor(c_known, known_message)

    # recover flag bytes using keystream (use ks up to length of c_flag)
    ks_for_flag = ks[:len(c_flag)]
    recovered = bxor(c_flag, ks_for_flag)

    try:
        print("Recovered flag (bytes):", recovered)
        print("Recovered flag (utf-8):", recovered.decode())
    except Exception:
        print("Recovered flag (bytes):", recovered)

if __name__ == "__main__":
    main()

