# WeirdSnake Challenge Writeup

## Challenge Overview
In this challenge, we were provided with a file containing Python bytecode disassembly. The task was to reverse engineer this bytecode to understand the program logic and extract the flag.

## Analysis

Upon examining the file, I identified that it contained Python bytecode disassembly from a file called "snake.py". The bytecode revealed several key operations:

1. Creation of an `input_list` with 40 integer values
2. Construction of a `key_str` through a series of string operations
3. Conversion of the key string to ASCII values stored in `key_list`
4. Extension of the key list to match the length of the input list
5. XOR operation between corresponding elements of both lists
6. Conversion of the resulting values to characters to form the flag

## Solution Approach

To solve this challenge, I reconstructed the original Python code from the bytecode:

```python
def solve_snake():
    # Step 1: Extract input_list
    input_list = [4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 102, 126, 92, 0, 16, 58, 41, 89, 78]
    
    # Step 2: Create key_str
    key_str = "J"
    key_str = "_" + key_str  # "_J"
    key_str = key_str + "o"  # "_Jo"
    key_str = key_str + "3"  # "_Jo3"
    key_str = "t" + key_str  # "t_Jo3"
    
    # Step 3: Convert key_str to key_list
    key_list = [ord(char) for char in key_str]  # [116, 95, 74, 111, 51]
    
    # Step 4: Extend key_list to match input_list length
    while len(key_list) < len(input_list):
        key_list.extend(key_list)
    key_list = key_list[:len(input_list)]  # Ensure exact length
    
    # Step 5: XOR the values and convert to characters
    result = [a ^ b for a, b in zip(input_list, key_list)]
    result_text = ''.join(map(chr, result))
    
    return result_text
```

### Key Observations:

1. The key string "t_Jo3" is built through a series of concatenation operations
2. The XOR operation is used as the encryption/decryption mechanism
3. The key is repeated to match the length of the encrypted data

## Execution and Flag

Running this solution code on the given input data yielded the flag:

```
picoCTF{N0t_sO_coNfus1ng_sn@ke_9433dec6}
```

## Conclusion

This challenge demonstrated the importance of understanding Python bytecode and common encryption techniques like XOR ciphers. By carefully analyzing the bytecode operations and reconstructing the original algorithm, we were able to reverse engineer the decryption process and retrieve the flag.

The "snake" theme in the challenge name not only refers to Python itself but also seems to play on the idea of "slithering" through obfuscated code to find the solution.
