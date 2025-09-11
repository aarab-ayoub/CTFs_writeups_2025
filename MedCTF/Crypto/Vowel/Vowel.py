def vowel_consonant_cipher(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    pos = 0  
    
    for char in text:
        if not char.isalpha():
            result.append(char)
            continue
            
        pos += 1
        original_lower = char.lower()
        base = ord('a') if char.islower() else ord('A')
        original_pos = ord(original_lower) - ord('a')
        
        if original_lower in vowels:
            new_pos = (original_pos + pos) % 26  # Vowels move forward
        else:
            new_pos = (original_pos - pos) % 26  # Consonants move backward
            
        result.append(chr(base + new_pos))
    
    return ''.join(result)

def vowel_consonant_decipher(ciphertext):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    pos = 0
    
    for char in ciphertext:
        if not char.isalpha():
            result.append(char)
            continue
            
        pos += 1
        encrypted_lower = char.lower()
        base = ord('a') if char.islower() else ord('A')
        encrypted_pos = ord(encrypted_lower) - ord('a')
        vowel_original_pos = (encrypted_pos - pos) % 26
        vowel_original_char = chr(ord('a') + vowel_original_pos)
        
        if vowel_original_char in vowels:
            new_pos = vowel_original_pos
        else:
            consonant_original_pos = (encrypted_pos + pos) % 26
            new_pos = consonant_original_pos
            
        result.append(chr(base + new_pos))
    
    return ''.join(result)

flag = "MED{v0w3ls_f0rw4rd_c0ns0n4nts_b4ckw4rd}"
print("Original:", flag)

ciphertext = vowel_consonant_cipher(flag)
print("Encrypted:", ciphertext)

decrypted = vowel_consonant_decipher(ciphertext)
print("Decrypted:", decrypted)