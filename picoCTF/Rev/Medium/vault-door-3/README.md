# Vault Door 3 Writeup

## Challenge Information
- **Name**: vault-door-3
- **Description**: This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java
- **Hint**: Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

## Understanding the Challenge

Looking at the provided `VaultDoor3.java` file, we can see that this challenge involves reverse engineering a password checking function. The code takes user input, removes the `picoCTF{` prefix and trailing `}`, and passes it to the `checkPassword` function.

The key to solving this challenge is understanding what the `checkPassword` function does. Let's analyze it:

```java
public boolean checkPassword(String password) {
    if (password.length() != 32) {
        return false;
    }
    char[] buffer = new char[32];
    int i;
    for (i=0; i<8; i++) {
        buffer[i] = password.charAt(i);
    }
    for (; i<16; i++) {
        buffer[i] = password.charAt(23-i);
    }
    for (; i<32; i+=2) {
        buffer[i] = password.charAt(46-i);
    }
    for (i=31; i>=17; i-=2) {
        buffer[i] = password.charAt(i);
    }
    String s = new String(buffer);
    return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
}
```

The function performs the following operations:
1. Checks if the password length is exactly 32 characters
2. Creates a buffer of 32 characters
3. Uses four different for loops to rearrange the characters from the password into the buffer
4. Compares the resulting buffer string with `"jU5t_a_sna_3lpm18gb41_u_4_mfr340"`

To solve this, we need to reverse the character scrambling process to determine what input would produce the expected output.

## Solution Approach

I wrote a Python script that reverses the operations performed in the `checkPassword` function:

```python
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
```

Here's how the script works:

1. We start with the target string `"jU5t_a_sna_3lpm18gb41_u_4_mfr340"` which represents the buffer after scrambling
2. For each of the four loops in the original code, we reverse the operation:
   - First loop (i=0 to 7): Direct mapping, so we copy characters directly
   - Second loop (i=8 to 15): The formula is `buffer[i] = password[23-i]`, so we reverse it to `password[23-i] = buffer[i]`
   - Third loop (i=16 to 31, step 2): The formula is `buffer[i] = password[46-i]`, so we reverse it to `password[46-i] = buffer[i]`
   - Fourth loop (i=31 to 17, step -2): The formula is `buffer[i] = password[i]`, so we reverse it to `password[i] = buffer[i]`
3. Finally, we add the `picoCTF{` prefix and `}` suffix to form the complete flag

## The Flag

Running the script produces the flag:
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
```

## Reflection

This challenge tested our ability to understand and reverse a character scrambling algorithm. The key insight was recognizing how each loop manipulated the characters and then working backwards to determine the original input that would yield the target string after scrambling.

The hint about making a table was helpful, as tracking the indices through each loop manually would have helped visualize how characters were being rearranged. However, by carefully analyzing the code and writing a reverse implementation, we were able to solve the challenge programmatically.
