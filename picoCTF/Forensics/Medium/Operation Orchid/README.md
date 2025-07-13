# Operation Orchid - PicoCTF Challenge Writeup

## Challenge Information
- **Name**: Operation Orchid
- **Category**: Forensics
- **Description**: Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
- **Files**: Compressed disk image

## Solution Overview

This challenge involves analyzing a disk image to recover an encrypted flag. The key to solving this challenge is understanding the encryption process used and finding the necessary information to reverse it.

## Step-by-Step Solution

### Step 1: Extract and Examine the Disk Image
After downloading and extracting the compressed disk image, we need to analyze its contents using forensic tools.

```bash
# Extract the compressed disk image
unzip [disk_image].zip
```

### Step 2: Open the Disk Image with FTK Imager
Using FTK Imager (or similar forensic tools), we can mount and explore the disk image file system to examine its contents.

```bash
# Alternative command-line approach (if using Linux tools)
# Mount the disk image or use tools like autopsy, sleuthkit, etc.
```

### Step 3: Explore the Root Directory
Upon examining the root directory of the disk image, we discover two important files:
- `flag.txt.enc` - The encrypted flag file
- `.ash_history` - Shell history file containing command history

### Step 4: Analyze the Shell History
The `.ash_history` file contains the command history that reveals how the flag was encrypted:

```bash
cat .ash_history
```

**Contents:**
```
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```

### Step 5: Understanding the Encryption Process
From the shell history, we can see:
1. A `flag.txt` file was created and edited
2. The file was encrypted using OpenSSL with AES-256 encryption
3. The encryption command used a salt and the password `unbreakablepassword1234567`
4. The original `flag.txt` was securely deleted using `shred -u`

**Key Information:**
- **Encryption Algorithm**: AES-256 with salt
- **Password**: `unbreakablepassword1234567`
- **Input File**: `flag.txt`
- **Output File**: `flag.txt.enc`

### Step 6: Decrypt the Flag
Now we can reverse the encryption process using the same OpenSSL command with the decrypt flag:

```bash
openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
```

**Output:**
```
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
4057AA7C027F0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:107:
```

Despite the warnings and error messages, the decryption process still works and creates the `flag.txt` file.

### Step 7: Retrieve the Flag
Finally, we can read the decrypted flag:

```bash
cat flag.txt
```

**Result:**
```
picoCTF{h4un71ng_p457_0a710765}
```

## Key Concepts Learned

1. **Disk Image Analysis**: Using forensic tools to examine disk images and file systems
2. **Shell History Forensics**: Analyzing command history files to understand user actions
3. **OpenSSL Encryption/Decryption**: Understanding symmetric encryption with AES-256
4. **Digital Forensics**: Recovering encrypted data when keys are available
5. **Evidence Recovery**: Finding crucial information in system artifacts

## Tools Used
- **FTK Imager** - For disk image analysis and file system exploration
- **OpenSSL** - For decrypting the AES-256 encrypted flag
- **Standard Linux commands** - For file manipulation and reading

## Command Reference

### OpenSSL Encryption (original)
```bash
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
```

### OpenSSL Decryption (solution)
```bash
openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
```

**Parameters:**
- `-d` - Decrypt mode
- `-salt` - Use salt in key derivation
- `-in` - Input file
- `-out` - Output file  
- `-k` - Password/key

## Alternative Approaches

1. **Using Autopsy**: Open the disk image in Autopsy for GUI-based analysis
2. **Sleuth Kit**: Use command-line tools like `fls`, `icat` for file system analysis
3. **Hex Editors**: Examine the encrypted file structure directly
4. **Other Forensic Tools**: Tools like Volatility (for memory dumps) or other specialized forensic suites

## Security Lessons

1. **Shell History Exposure**: Command history files can reveal sensitive information including passwords
2. **Weak Key Management**: Storing encryption keys in command history is a security vulnerability
3. **Secure Deletion**: The `shred` command was used to securely delete the original file
4. **Deprecated Methods**: OpenSSL warns about deprecated key derivation methods

## Flag
```
picoCTF{h4un71ng_p457_0a710765}
```

## Conclusion

This challenge demonstrates the importance of proper digital forensics techniques and highlights how system artifacts like shell history can contain crucial information for recovering encrypted data. The challenge emphasizes that even with strong encryption, poor operational security (like leaving passwords in command history) can compromise the entire system.
