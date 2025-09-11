# Seeded Flag Generator Challenge - Writeup

## Challenge Overview

This challenge presents a C program that generates a flag based on a specific seed value. The program employs anti-debugging techniques and expects the user to determine the correct flag without using debugging tools.

## Understanding the Code

The program consists of several key components:

1. **Anti-Debugging Mechanism**: The `anti_debug()` function checks if the process is being traced by examining the `/proc/self/status` file for a non-zero `TracerPid`.

2. **Seed Validation**: The `check_seed()` function verifies that the provided key matches the magic number `3735928559` (which is `0xDEADBEEF` in hexadecimal).

3. **Flag Generation**: The `build_flag()` function constructs a flag string using various bitwise operations on the seed value.

4. **Flag Verification**: The `verify_flag()` function compares the user's input against the generated flag.

## Solution Approach

The challenge can be solved by understanding how the flag is constructed from the seed value in the `build_flag()` function. Since we know the seed must be `0xDEADBEEF`, we can calculate what the flag should be by analyzing the operations performed on each character.

### Key Insights:

- The seed value must be `0xDEADBEEF` (3735928559 in decimal)
- The flag format follows a pattern where each character is derived from operations on the seed
- By analyzing the first few characters, we can confirm the flag starts with "MED{"

### Breaking Down the Flag Construction

Let's look at how the first few characters are calculated:

```c
buffer[0] = (seed >> 24) - 0x91;  // (0xDE >> 24) - 0x91 = 0xDE - 0x91 = 0x4D = 'M'
buffer[1] = (seed >> 16) - 0x68;  // (0xDEAD >> 16) - 0x68 = 0xAD - 0x68 = 0x45 = 'E'
buffer[2] = (seed >> 8) - 0x7A;   // (0xDEADBE >> 8) - 0x7A = 0xBE - 0x7A = 0x44 = 'D'
buffer[3] = seed - 0x74;          // (Lowest byte of 0xDEADBEEF) - 0x74 = 0xEF - 0x74 = 0x7B = '{'
```

Continuing this pattern and tracking all operations, we can determine the complete flag.

## The Flag

After calculating all buffer values according to the operations in `build_flag()`, the resulting flag is:

```
MED{H3_wh0_c1e4n5_h15_h0u53_3xp3c75_v15170r5}
```

## Challenge Summary

This reverse engineering challenge requires:
1. Identifying the correct seed value (`0xDEADBEEF`)
2. Understanding the flag generation algorithm
3. Calculating the flag characters based on operations applied to the seed
4. Bypassing or avoiding the anti-debugging measure

The flag appears to be a modified version of the quote: "He who cleans his house expects visitors."

## Tools and Techniques Used

- Static analysis of the C code
- Manually tracing the calculations for each character
- Understanding bitwise operations and hexadecimal representations