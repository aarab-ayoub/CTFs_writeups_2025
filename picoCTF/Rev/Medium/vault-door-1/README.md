# vault-door-1 - Reverse Engineering Challenge Writeup

## Challenge Description
This vault uses some complicated arrays! I hope you can make sense of it, special agent.

## Hint
Look up the charAt() method online.

## Solution

In this challenge, we are provided with a Java source code file named `VaultDoor1.java`. The goal is to determine the correct password by analyzing the validation method in the code.

### Analysis of the Source Code

Here's the provided code:

```java
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               // ... (more character checks)
               password.charAt(31) == 'e';
    }
}
```

The key observations:
1. The code strips `picoCTF{` from the beginning and `}` from the end of the user input
2. The password must be exactly 32 characters long
3. The `checkPassword` method validates each character of the password at specific positions

The challenge is to reconstruct the correct password by reorganizing the character checks into their proper sequence.

### Step 1: Extract Character Position Information

I examined all the charAt() conditions in the checkPassword method and created a mapping of character positions to their expected values:

```
password.charAt(0)  == 'd'
password.charAt(1)  == '3'
password.charAt(2)  == '5'
password.charAt(3)  == 'c'
password.charAt(4)  == 'r'
...and so on
```

### Step 2: Create a Script to Reconstruct the Password

I wrote a Python script to reconstruct the password by placing each character at its correct position:

```python
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
```

### Step 3: Run the Script to Get the Flag

Executing the script outputs the complete flag:

```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}
```

## Flag
`picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}`

## Learning Points
- Understanding Java string manipulation methods like charAt()
- Recognizing that sometimes security through obscurity (scrambling characters) is not effective
- How to reconstruct data when given position-specific information
- Creating scripts to automate the reconstruction of scrambled information
- Reverse engineering doesn't always require complex decompilation - sometimes it's just about understanding the logic
