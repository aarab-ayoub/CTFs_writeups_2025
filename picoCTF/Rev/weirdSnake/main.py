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

# Get the flag
flag = solve_snake()
print(f"Flag: {flag}")
