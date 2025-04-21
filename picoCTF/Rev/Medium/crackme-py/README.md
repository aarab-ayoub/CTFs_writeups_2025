# crackme-py - Reverse Engineering Challenge Writeup

## Challenge Description
No description provided. The challenge includes a Python file called `crackme.py` that we need to analyze to find the flag.

## Solution

This challenge provides us with a Python script that we need to reverse engineer to find the hidden flag.

### Analysis of the Source Code

Let's examine the provided Python file:

```python
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0g4dd`_cgN"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)

def choose_greatest():
    """Echo the largest of the two numbers given by the user to the program

    Warning: this function was written quickly and needs proper error handling
    """

    user_value_1 = input("What's your first number? ")
    user_value_2 = input("What's your second number? ")
    greatest_value = user_value_1 # need a value to return if 1 & 2 are equal

    if user_value_1 > user_value_2:
        greatest_value = user_value_1
    elif user_value_1 < user_value_2:
        greatest_value = user_value_2

    print( "The number with largest positive magnitude is "
        + str(greatest_value) )

choose_greatest()
```

After analyzing the code, I noticed:

1. There's an encrypted string `bezos_cc_secret` that likely contains the flag
2. A function called `decode_secret()` is defined that performs a ROT47 decoding operation
3. However, only the `choose_greatest()` function is called when the script runs
4. The `decode_secret()` function is never called with the `bezos_cc_secret` string

### Method 1: Modifying the Script

The simplest solution is to modify the script to call the `decode_secret()` function with the encrypted string. At the end of the file, I added:

```python
decode_secret(bezos_cc_secret)
```

Then I ran the modified script:

```
$ python3 crackme.py 
What's your first number? 1
What's your second number? 2
The number with largest positive magnitude is 2
picoCTF{1|\/|_4_p34|\|ut_8c551048}
```

The script first executed the `choose_greatest()` function (which was irrelevant to finding the flag), and then executed our added line to decode and print the secret, revealing the flag.

### Method 2: Using CyberChef

Alternatively, since the code reveals that the encryption is ROT47, we can use an online tool like CyberChef to decode the string:

1. Input the encrypted string: `A:4@r%uL`M-^M0c0AbcM-MFE0g4dd`_cgN`
2. Apply the ROT47 operation
3. The result is the flag: `picoCTF{1|\/|_4_p34|\|ut_8c551048}`

## Flag
`picoCTF{1|\/|_4_p34|\|ut_8c551048}`

## Learning Points
- Always analyze all functions in the provided code, even if they're not called
- Look for encrypted strings or data that might contain the flag
- Understanding basic ciphers like ROT (rotation) ciphers
- Multiple approaches can be used to solve a challenge (code modification vs. external tools)
- Sometimes the challenge includes misdirection (the `choose_greatest()` function was irrelevant)
