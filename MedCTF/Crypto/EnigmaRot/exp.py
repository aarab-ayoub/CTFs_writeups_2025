import base64

flag = "MED{k4nt_jd4t1_t4tg0l_1t_1s_wh4t_1t_1s}"

def rot_shift_char(c, shift):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    else:
        return c

def reverse_rot_shift_char(c, shift):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
    else:
        return c  

def rev_apply_rot_shifts(data: str) -> str:
    result = []
    result.append("MED")
    for i, c in enumerate(data[3:], start=3): 
        if i % 2 == 0: 
            result.append(reverse_rot_shift_char(c, 1337))
        else:
            result.append(reverse_rot_shift_char(c, 42))
    return ''.join(result)


def apply_rot_shifts(data: str) -> str:
    result = []
    result.append("MED") 
    for i, c in enumerate(data[3:], start=3): 
        if i % 2 == 0: 
            result.append(rot_shift_char(c, 1337))
        else:
            result.append(rot_shift_char(c, 42))
    return ''.join(result)


rot_shifted_flag = apply_rot_shifts(flag)
print(f"Rotated flag: {rot_shifted_flag}")
decode = "MED{v4yj_zo4e1_j4jr0w_1j_1d_hx4j_1e_1i}"
out = rev_apply_rot_shifts(decode)
print(f"Decrypted flag: {out}")



