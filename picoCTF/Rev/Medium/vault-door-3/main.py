def reverse_vault_door3():
    s = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
    buffer = list(s)
    password = [''] * 32

    # buffer[0..7] = password[0..7]
    for i in range(8):
        password[i] = buffer[i]

    # buffer[8..15] = password[15..8] => password[23 - i] = buffer[i]
    for i in range(8, 16):
        password[23 - i] = buffer[i]

    # buffer[16,18,20,...30] = password[46 - i]
    for i in range(16, 32, 2):
        password[46 - i] = buffer[i]

    # buffer[17,19,...,31] = password[i]
    for i in range(31, 16, -2):
        password[i] = buffer[i]

    flag = "picoCTF{" + ''.join(password) + "}"
    return flag

print(reverse_vault_door3())

