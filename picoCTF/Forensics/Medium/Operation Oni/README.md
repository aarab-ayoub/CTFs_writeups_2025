# Operation Oni - PicoCTF Challenge Writeup

## Challenge Information
- **Name**: Operation Oni
- **Category**: Forensics
- **Description**: Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
- **Files**: Disk image
- **Remote Target**: `ssh -i key_file -p 50992 ctf-player@saturn.picoctf.net`

## Solution Overview

This challenge involves analyzing a disk image to recover SSH private keys, then using those keys to authenticate to a remote server and retrieve the flag. The solution demonstrates digital forensics techniques combined with SSH key management.

## Step-by-Step Solution

### Step 1: Extract and Analyze the Disk Image
Download and extract the provided disk image file.

```bash
# Extract the disk image
unzip [disk_image].zip
```

### Step 2: Mount and Explore the Disk Image
Using forensic tools like FTK Imager or command-line tools, explore the file system structure of the disk image.

### Step 3: Examine Shell History
Navigate to the root directory and examine the `.ash_history` file to understand what commands were executed on the system.

```bash
cat .ash_history
```

The shell history reveals SSH key generation commands, indicating that SSH keys were created on this system.

### Step 4: Locate SSH Keys
Based on the shell history, navigate to the SSH directory (typically `.ssh/` in the user's home directory or `/root/.ssh/`) to find the SSH key files.

**Files found:**
- `id_ed25519` - Private key file
- `id_ed25519.pub` - Public key file

### Step 5: Extract the Private Key
Copy the private key file (`id_ed25519`) from the disk image to your local system for use in SSH authentication.

### Step 6: Fix Key Permissions
SSH requires private key files to have restrictive permissions. The initial attempt fails due to incorrect permissions:

```bash
ssh -i id_ed25519 -p 53670 ctf-player@saturn.picoctf.net
```

**Error Output:**
```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for 'id_ed25519' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "id_ed25519": bad permissions
ctf-player@saturn.picoctf.net's password:
```

**Solution:** Fix the permissions using `chmod`:

```bash
chmod 600 id_ed25519
```

### Step 7: SSH Authentication and Flag Retrieval
With correct permissions, authenticate using the private key:

```bash
ssh -i id_ed25519 -p 53670 ctf-player@saturn.picoctf.net
```

**Successful Connection:**
```
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$
```

### Step 8: Retrieve the Flag
Once connected, locate and read the flag:

```bash
ls
cat flag.txt
```

**Result:**
```
picoCTF{k3y_5l3u7h_339601ed}
```

## Key Concepts Learned

1. **Digital Forensics**: Analyzing disk images to recover authentication credentials
2. **SSH Key Management**: Understanding public/private key pairs and their usage
3. **File Permissions**: Importance of correct permissions for SSH private keys
4. **Shell History Analysis**: Using command history to understand system activities
5. **Remote Authentication**: Using recovered keys for SSH authentication

## Tools Used
- **FTK Imager** or similar forensic tools for disk image analysis
- **SSH client** for remote authentication
- **chmod** for setting correct file permissions
- **Standard Linux commands** for file system navigation

## SSH Key Types
The challenge uses **Ed25519** keys:
- **Private Key**: `id_ed25519` (must be kept secret)
- **Public Key**: `id_ed25519.pub` (can be shared)
- **Algorithm**: Ed25519 (modern, secure elliptic curve cryptography)

## File Permissions Reference
SSH private keys require specific permissions:
- **Correct Permission**: `600` (read/write for owner only)
- **Incorrect Permission**: `664` (readable by group and others)
- **Command**: `chmod 600 private_key_file`

## Security Implications

1. **Key Storage**: SSH private keys should be stored securely and with proper permissions
2. **Forensic Recovery**: Private keys left on disk images can be recovered by attackers
3. **Access Control**: Proper file permissions are critical for SSH security
4. **Key Management**: Organizations should have policies for SSH key lifecycle management

## Alternative Approaches

1. **Command-line Forensics**: Using tools like `sleuthkit` instead of GUI tools
2. **Automated Key Discovery**: Scripts to search for SSH keys across file systems
3. **Memory Forensics**: If the system was compromised, keys might be in memory dumps
4. **Network Forensics**: Analyzing network traffic for SSH key exchanges

## Common SSH Key Locations
- `/home/user/.ssh/`
- `/root/.ssh/`
- `/etc/ssh/`
- Custom locations specified in SSH configuration

## Flag
```
picoCTF{k3y_5l3u7h_339601ed}
```

## Conclusion

This challenge demonstrates the intersection of digital forensics and system administration. It highlights how SSH keys recovered from disk images can be used to gain unauthorized access to systems. The challenge also reinforces the importance of proper file permissions in SSH security and shows how forensic analysis of shell history can reveal critical information about system activities and security configurations.
