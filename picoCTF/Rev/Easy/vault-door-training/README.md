# vault-door-training - Reverse Engineering Challenge Writeup

## Challenge Description
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility.

## Hint
The password is revealed in the program's source code.

## Solution

This challenge provides us with a Java source code file named `VaultDoorTraining.java`. Our task is to read through the code to identify the password that will open the vault door.

### Analysis of the Source Code

Let's examine the provided Java file:

```java
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
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

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_3808d338b46");
    }
}
```

Looking at this code:

1. The program prompts the user to enter a password
2. It strips off the `picoCTF{` prefix and the closing `}` from the user input
3. It passes the inner content to the `checkPassword` method
4. The `checkPassword` method compares this inner content with a hardcoded string

### Finding the Password

In the `checkPassword` method, we can see the following line:

```java
return password.equals("w4rm1ng_Up_w1tH_jAv4_3808d338b46");
```

This clearly shows that the expected password is `"w4rm1ng_Up_w1tH_jAv4_3808d338b46"`.

Given that the program strips the `picoCTF{` prefix and the closing `}` before checking, the full flag format must be:

```
picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}
```

## Flag
`picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}`

## Learning Points
- This challenge demonstrates a basic principle of security: Never hardcode sensitive information like passwords directly in the source code
- Reading and understanding source code is a fundamental skill in reverse engineering
- This is an example of "security through obscurity," which is not a strong security practice
- Even in simple challenges, it's important to understand how the program processes input (in this case, stripping the flag format) to format your answer correctly
