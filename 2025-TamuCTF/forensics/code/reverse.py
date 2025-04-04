import numpy as np
import base64

binary_array = np.array([
    [[0., 1., 0., 1., 0., 1., 1., 0., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 1., 1., 0., 0., 1.,
    0., 0., 1., 1., 0., 0.,],
    [1., 1., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1., 0., 1., 0., 0., 1., 1., 0., 1., 0., 0., 0., 1.,
    0., 1., 0., 1., 1., 0.,],
    [1., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1., 0., 1., 0., 0., 1., 1., 0., 1., 0., 0.,
    0., 1., 0., 1., 0., 1.,],
    [1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1., 0., 1., 0., 0., 1., 1., 0., 1.,
    0., 0., 0., 1., 0., 1.,],
    [0., 1., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 1., 1., 0.,
    0., 1., 1., 0., 1., 1.,],
    [0., 0., 0., 1., 1., 1., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0., 0.,
    1., 1., 0., 1., 0., 0.,],
    [0., 0., 1., 0., 0., 1., 1., 1., 0., 0., 0., 1., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 1.,
    1., 0., 0., 0., 0., 1.,],
    [0., 0., 1., 1., 1., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1.,
    0., 0., 0., 1., 1., 1.,],
    [0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 1., 1., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0.,
    0., 1., 0., 0., 0., 0.,],
    [1., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0.,
    0., 1., 0., 1., 0., 0.,],
    [0., 1., 1., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 1., 0., 0., 1., 1., 1., 0., 1., 1., 0.,
    0., 0., 1., 0., 0., 1.,],
    [0., 1., 0., 1., 1., 1., 0., 1., 0., 1., 0., 1., 1., 0., 0., 1., 1., 1., 1., 0., 1., 0., 0., 1.,
    1., 0., 0., 0., 1., 1.,],
    [0., 0., 1., 1., 0., 0., 1., 0., 0., 1., 0., 0., 0., 1., 1., 0., 0., 1., 1., 0., 1., 1., 1., 0.,
    0., 1., 0., 1., 1., 0.,],
    [1., 0., 0., 1., 0., 1., 0., 0., 1., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 1., 1., 0., 1., 0.,
    0., 0., 0., 1., 1., 0.,],
    [0., 0., 1., 0., 0., 1., 1., 0., 1., 1., 0., 1., 0., 1., 0., 1., 0., 0., 0., 1., 0., 1., 1., 0.,
    0., 1., 1., 1., 0., 1.,],
    [1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 1., 1., 1., 0., 1., 1., 0., 1., 0., 0., 0., 0., 1.,
    1., 0., 1., 1., 0., 0.,],
    [0., 1., 0., 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 1., 1., 1., 0., 1., 0., 1., 1., 0., 1., 0.,
    0., 1., 1., 1., 0., 0.,],
    [1., 1., 0., 1., 0., 1., 1., 0., 0., 1., 0., 1., 0., 1., 0., 1., 1., 1., 0., 1., 1., 0., 0., 0.,
    1., 1., 0., 0., 1., 1.,],
    [0., 1., 1., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 1., 1., 1., 0., 1., 1., 0.,
    0., 1., 0., 0., 0., 1.,],
    [1., 1., 0., 0., 0., 0., 0., 1., 0., 1., 1., 0., 1., 0., 0., 0., 1., 1., 0., 0., 1., 0., 0., 1.,
    0., 1., 0., 1., 1., 0.,],
    [0., 1., 1., 1., 0., 1., 0., 0., 0., 1., 1., 0., 0., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1., 0.,
    0., 1., 0., 0., 1., 0.,],
    [0., 1., 0., 1., 1., 1., 1., 0., 0., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 1., 1., 0., 1., 0.,
    1., 0., 0., 1., 0., 1.,],
    [0., 0., 1., 0., 0., 1., 1., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 0., 1., 0., 1., 0., 1.,
    0., 1., 1., 0., 0., 0.,],
    [1., 1., 1., 0., 0., 1., 0., 1., 1., 0., 1., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 1., 0., 0.,
    1., 1., 0., 0., 1., 0.,],
    [0., 1., 0., 0., 1., 1., 0., 1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 0., 1., 1., 0., 1., 0.,
    0., 1., 0., 0., 0., 1.,],
    [0., 0., 0., 1., 0., 0., 0., 1., 1., 0., 0., 1., 1., 1., 0., 1., 0., 1., 0., 1., 0., 0., 1., 1.,
    1., 0., 0., 1., 1., 0.,],
    [1., 1., 0., 0., 0., 0., 1., 1., 1., 0., 0., 1., 0., 1., 1., 0., 1., 1., 1., 1., 0., 1., 0., 0.,
    1., 1., 0., 1., 0., 1.,],
    [1., 1., 1., 0., 1., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0., 0., 1., 1., 0., 1., 0., 1., 0., 1.,
    1., 0., 0., 1., 0., 1.,],
    [0., 1., 0., 1., 0., 1., 0., 0., 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 1., 1., 0., 1., 1., 0.,
    0., 1., 0., 0., 1., 1.,],
    [1., 1., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.,
    0., 1., 0., 0., 0., 0.,]]
])

flattened_binary = binary_array.flatten()

binary_string = ''.join(map(str, flattened_binary.astype(int)))

decoded_text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

print("Decoded Flag:", decoded_text)

print("Base64 Decoded Flag:", base64.b64decode(decoded_text).decode())
