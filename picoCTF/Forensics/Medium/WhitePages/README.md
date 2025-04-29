# CTF Challenge: WhitePages

## Challenge Description
I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

## Solution Approach

### Step 1: Inspecting the File
After downloading the provided `whitepages.txt` file, I opened it in a text editor, but it appeared completely blank. The challenge name "WhitePages" and description hint that there's hidden information in what appears to be an empty file.

To investigate further, I examined the hexadecimal representation of the file using the `xxd` command:

```bash
$ xxd -g 1 whitepages.txt
```

Output:
```
00000000: e2 80 83 e2 80 83 e2 80 83 e2 80 83 20 e2 80 83  ............ ...
00000010: 20 e2 80 83 e2 80 83 e2 80 83 e2 80 83 e2 80 83   ...............
00000020: 20 e2 80 83 e2 80 83 20 e2 80 83 e2 80 83 e2 80   ...... ........
```

This revealed that the file wasn't empty at all! Instead, it contained two repeating patterns:
- `e2 80 83`: Unicode EM SPACE character
- `20`: Standard ASCII space character

### Step 2: Understanding the Hidden Pattern
Upon examining these patterns, I realized this could be a binary encoding system:
- The Unicode EM SPACE (`e2 80 83`) could represent a `0`
- The standard ASCII space (`20`) could represent a `1`

This pattern of two distinct space characters suggested a binary encoding scheme where the content was hidden using spaces that look identical but have different byte representations.

### Step 3: Decoding the Hidden Binary Data
To decode this hidden message, I created a Python script to convert these spaces into binary, then transform the binary data to ASCII:

```python
def convertSpacesToBinary():
    with open('whitepages.txt', 'rb') as f:
        result = f.read()
    result = result.replace(b'\xe2\x80\x83', b'0')  # Unicode EM SPACE -> 0
    result = result.replace(b'\x20', b'1')  # ASCII Space -> 1
    result = result.decode()
    return result

print(convertSpacesToBinary())
```

Running this script gave me a binary string. I then used CyberChef with the "From Binary" operation to convert this binary data to ASCII text.

### Step 4: Retrieving the Flag
The decoded message revealed:

```
		picoCTF

		SEE PUBLIC RECORDS & BACKGROUND REPORT
		5000 Forbes Ave, Pittsburgh, PA 15213
		picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}
```

## Tools Used
- Text editor (Kate/Sublime)
- `xxd` command-line tool
- Python for custom script
- CyberChef for binary-to-ASCII conversion

## Conclusion
This challenge demonstrates a creative form of steganography using different types of whitespace characters to encode information. It reminds us that not all spaces are the same in computing, even though they may appear identical visually. The solution required understanding how different Unicode characters can be leveraged for binary encoding.

## Flag
`picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}`
