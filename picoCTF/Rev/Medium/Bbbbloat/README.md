# Bbbbloat Writeup

## Challenge Information
- **Name**: Bbbbloat
- **Description**: Can you get the flag? Reverse engineer this binary.

## Understanding the Challenge

This challenge provides a binary file named `bbbbloat` that we need to reverse engineer to find the flag. When running the binary, it asks for a "favorite number":

```
./bbbbloat 
What's my favorite number? 123
Sorry, that's not it!
```

The program is looking for a specific input value. If we provide the wrong value, it responds with "Sorry, that's not it!". This suggests that we need to find the correct number to get the flag.

## Solution Approach #1: Static Analysis

I decompiled the binary to examine its logic. The main function looks like this:

```c
undefined8 main(int argc, char **argv)
{
    int64_t in_FS_OFFSET;
    char **var_58h;
    int var_4ch;
    int32_t var_48h;
    int64_t var_44h;
    int64_t var_38h;
    int64_t var_30h;
    int64_t var_28h;
    int64_t var_20h;
    int64_t canary;
    
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    var_38h = 0x4c75257240343a41;
    var_30h = 0x3062396630664634;
    var_28h = 0x65623066635f3d33;
    var_20h = 0x4e326560623535;
    var_44h._0_4_ = 0xd2c49;
    printf("What\'s my favorite number? ");
    var_44h._0_4_ = 0xd2c49;
    __isoc99_scanf(data.00002020, &var_48h);
    var_44h._0_4_ = 0xd2c49;
    if (var_48h == 0x86187) {
        var_44h._0_4_ = 0xd2c49;
        *(undefined8 *)0x0 = fcn.00001249(0, (char *)&var_38h);
        fputs(*(undefined8 *)0x0, _stdout);
        putchar(10);
        free(stack0xffffffffffffffc0);
    } else {
        puts("Sorry, that\'s not it!");
    }
    if (canary != *(int64_t *)(in_FS_OFFSET + 0x28)) {
    // WARNING: Subroutine does not return
        __stack_chk_fail();
    }
    return 0;
}
```

The key part of this code is the conditional statement:

```c
if (var_48h == 0x86187)
```

Here we can see that the program is checking if our input equals `0x86187`, which is a hexadecimal value. Converting this to decimal:

```
0x86187 = 549255
```

So the "favorite number" the program is looking for is 549255.

## Testing the Solution

Running the program with this input:

```
./bbbbloat 
What's my favorite number? 549255
picoCTF{cu7_7h3_bl047_36dd316a}
```

And there we have it! The flag is `picoCTF{cu7_7h3_bl047_36dd316a}`.

## Solution Approach #2: Deeper Analysis

For a deeper understanding, I also looked at the function `fcn.00001249` which processes the flag before displaying it:

```c
int64_t fcn.00001249(int64_t arg1, char *arg2)
{
    char cVar1;
    int32_t iVar2;
    int64_t iVar3;
    uint64_t uVar4;
    char *src;
    int64_t var_30h;
    int64_t var_20h;
    char *s;
    size_t var_10h;
    
    iVar3 = strdup(arg2);
    uVar4 = strlen(iVar3);
    for (var_20h = 0; (uint64_t)var_20h < uVar4; var_20h = var_20h + 1) {
        if ((' ' < *(char *)(var_20h + iVar3)) && (*(char *)(var_20h + iVar3) != '\x7f')) {
            iVar2 = *(char *)(var_20h + iVar3) + 0x2f;
            cVar1 = (char)iVar2;
            if (iVar2 < 0x7f) {
                *(char *)(var_20h + iVar3) = cVar1;
            } else {
                *(char *)(var_20h + iVar3) = cVar1 + -0x5e;
            }
        }
    }
    return iVar3;
}
```

This function performs character manipulation on a string:

1. It duplicates the input string using `strdup()`
2. For each character in the string that is:
   - Greater than space (ASCII 32)
   - Not the DEL character (ASCII 127)
3. It performs a transformation:
   - Adds 0x2F (47) to the character's ASCII value
   - If the result is less than 0x7F (127), it keeps that value
   - If the result is 0x7F or greater, it subtracts 0x5E (94)

I noticed that the program initializes these variables with what appears to be encrypted flag data:

```c
var_38h = 0x4c75257240343a41;
var_30h = 0x3062396630664634;
var_28h = 0x65623066635f3d33;
var_20h = 0x4e326560623535;
```

These values are in little-endian format. When converted to a readable byte sequence, they become:

```
41 3a 34 40 72 25 75 4c 34 46 66 30 66 39 62 30 33 3d 5f 63 66 30 62 65 35 35 62 60 65 32 4e
```

Which corresponds to the ASCII string:
```
A:4@r%uL4Ff0f9b03=_cf0be55b`e2N
```

This is the encrypted version of the flag. To decrypt it, I needed to reverse the transformation logic:

1. For each byte, if it's not a space and not 0x7F:
   - Subtract 0x2F (47)
   - If the result is below 0x20 (32), add 0x5E (94) to wrap around
2. Otherwise, keep the byte as-is

I implemented this decryption logic in Python:

```python
encrypted_bytes = bytes.fromhex("41 3a 34 40 72 25 75 4c 34 46 66 30 66 39 62 30 33 3d 5f 63 66 30 62 65 35 35 62 60 65 32 4e")
decrypted = []

for byte in encrypted_bytes:
    if byte > 0x20 and byte != 0x7F:  # Same conditions as in the original function
        # Reverse the transformation (subtract 47, wrap around modulo 94)
        decrypted_byte = byte - 0x2F
        if decrypted_byte < 0x20:  # If subtraction goes below 0x20, wrap around
            decrypted_byte += 0x5E
        decrypted.append(decrypted_byte)
    else:
        decrypted.append(byte)  # Leave spaces and DEL unchanged

# Convert back to a string
flag = bytes(decrypted).decode('ascii')
print(f"Decrypted flag: {flag}")
```

Running this script confirmed the flag:

```
Decrypted flag: picoCTF{cu7_7h3_bl047_36dd316a}
```

## Reflection

This challenge demonstrates the importance of binary analysis in CTF competitions. There were two viable approaches:

1. The simple approach: finding the magic number that the program is looking for by inspecting the decompiled code.
2. The in-depth approach: understanding the encryption logic and directly decrypting the flag data stored in the binary.

Both approaches lead to the same flag, but the second method gives us a better understanding of the program's internal workings.

The challenge name "Bbbbloat" likely refers to the fact that the binary contains much more complex code than necessary for its relatively simple functionality - a common technique used to make reverse engineering more challenging.
