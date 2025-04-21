def recover_password():
    password = [''] * 32

    known_positions = {
        0: 'd',
        1: '3',
        2: '5',
        3: 'c',
        4: 'r',
        5: '4',
        6: 'm',
        7: 'b',
        8: 'l',
        9: '3',
        10: '_',
        11: 't',
        12: 'H',
        13: '3',
        14: '_',
        15: 'c',
        16: 'H',
        17: '4',
        18: 'r',
        19: '4',
        20: 'c',
        21: 'T',
        22: '3',
        23: 'r',
        24: '5',
        25: '_',
        26: '7',
        27: '5',
        28: '0',
        29: '9',
        30: '2',
        31: 'e'
    }

    for index, char in known_positions.items():
        password[index] = char

    return "picoCTF{" + ''.join(password) + "}"

print(recover_password())

