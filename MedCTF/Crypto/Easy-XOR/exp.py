import base64


flag = "MED{x0r_with_m34n1ngl3ss_k3y}"


def xor_with_key(data: str, key: str) -> str:
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))


def base32_encode_n_times(input_string: str, n: int) -> str:
    encoded = input_string.encode('utf-8')
    for _ in range(n):
        encoded = base64.b32encode(encoded)
    return encoded.decode('utf-8')


def add_padding(encoded_string: str) -> str:
    while len(encoded_string) % 8 != 0:
        encoded_string += '='
    return encoded_string


xor_result = xor_with_key(flag, "MED")


base32_result = base32_encode_n_times(xor_result, 5)

print(f"Base32 encoded XOR result: {base32_result}")


decode = add_padding(base32_result)

for _ in range(5):
    decode = base64.b32decode(decode)

result = xor_with_key(decode.decode('utf-8'), "MED")

print(f"Recovered flag: {result}")