from PIL import Image
import base64
import random

def hide_data_in_lsb(image_path, data_to_hide, output_path):
    """
    Hide data in the least significant bit of the image using a more 
    detectable pattern that will show up in zsteg.
    """
    # Load the image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    
    # Convert data to binary
    # First add a recognizable header to make it easier to spot
    data_to_hide = "CALMABOT:" + data_to_hide
    binary_data = ''.join(format(ord(char), '08b') for char in data_to_hide)
    
    # Counter for binary data position
    binary_index = 0
    
    # Pattern: modify only blue channel in first 100 rows
    # This creates a pattern that's more likely to be detected by zsteg
    for y in range(min(100, height)):
        for x in range(width):
            if binary_index < len(binary_data):
                r, g, b = pixels[x, y]
                
                # Modify only the LSB of the blue channel
                b = (b & 0xFE) | int(binary_data[binary_index])
                
                pixels[x, y] = (r, g, b)
                binary_index += 1
                
                # Break if we've hidden all the data
                if binary_index >= len(binary_data):
                    break
    
    # Save the modified image
    img.save(output_path, "PNG")
    
    return "Data hidden successfully in LSB of blue channel"

def add_passphrase_to_comment(image_path, passphrase, output_path):
    """Add the passphrase as an encrypted comment in the image."""
    from PIL import Image, PngImagePlugin
    
    # Load the image
    img = Image.open(image_path)
    
    # Create a simple cipher for the passphrase - ROT13 with hex
    def rot13_hex(text):
        result = ""
        for char in text:
            if 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                result += char
        
        # Convert to hex with separators
        return ':'.join(hex(ord(c))[2:] for c in result)
    
    encrypted_passphrase = rot13_hex(passphrase)
    
    # Create metadata dictionary
    meta = PngImagePlugin.PngInfo()
    
    # Add the encrypted passphrase as a comment with a hint
    meta.add_text("Comment", f"Ronaldo says: Calma, calma! The secret lies in the celebration... ")
    meta.add_text("artist", encrypted_passphrase)
    
    # Save the image with metadata
    img.save(output_path, "PNG", pnginfo=meta)
    
    return f"Passphrase hidden in metadata as ROT13+hex: {encrypted_passphrase}"

def main():
    # Define paths
    original_image = "calma.jpg"
    output_image = "ronaldo_calma.png"
    
    # Bot information to hide
    bot_username = "Gdvsusbsjbot"
    bot_token = "8118975932:AAEx5L5lnJTxncPKmlqud4j08qv0Y4m7fIQ"
    data_to_hide = f"{bot_username}|{bot_token}"
    
    # Passphrase to find
    passphrase = "calma calma!"
    
    # First, hide the bot info in the LSB
    print(hide_data_in_lsb(original_image, data_to_hide, "temp_steg.png"))
    
    # Then, add the passphrase as an encrypted comment
    print(add_passphrase_to_comment("temp_steg.png", passphrase, output_image))
    
    print(f"\nChallenge image created: {output_image}")
    print("Expected zsteg output will show 'CALMABOT:' in the LSB scan")
    print("Expected exiftool output will show an encrypted comment")

if __name__ == "__main__":
    main()