import base64
import string

# Extracted from VBA code
secret_data = [89, 90, 91, 74, 106, 55, 91, 57, 94, 55, 91, 120, 93, 55, 54, 109, 94, 108, 69, 123, 93, 55, 95, 120, 94, 92, 105, 62]
shift = 5

# Reverse the shift to get ASCII values
ascii_values = [x - shift for x in secret_data]

# Convert to Base64 string
base64_string = ''.join(chr(x) for x in ascii_values)
print("Base64 string:", base64_string)

# Replace invalid characters in Base64 string
base64_string = base64_string.replace('@', '/')

# Ensure proper padding
if len(base64_string) % 4 != 0:
    base64_string += '=' * (4 - len(base64_string) % 4)

# Decode the Base64 string
try:
    decoded_bytes = base64.b64decode(base64_string)
    print("Decoded bytes:", decoded_bytes)

    # Extract printable characters to reconstruct the flag
    printable_bytes = bytes(c for c in decoded_bytes if chr(c) in string.printable)
    flag = printable_bytes.decode('utf-8', errors='ignore')  # Ignore non-UTF-8 characters
    print("Flag:", flag)
except UnicodeDecodeError as e:
    print("UTF-8 decoding error:", e)
    print("Decoded bytes (raw):", decoded_bytes)
except Exception as e:
    print("Error:", e)