# DISKO 1 Challenge Writeup

## Challenge Overview

**Challenge Name:** DISKO 1  
**Category:** Forensics  
**Description:** Can you find the flag in this disk image? Download the disk image here.  
**Hint:** Maybe Strings could help? If only there was a way to do that?

This is an introductory forensics challenge focusing on basic disk image analysis using string extraction.

## Files Provided

- `disko-1.dd` - Disk image file

## Analysis

### 1. File Type Identification

First, let's identify what we're working with:

```bash
$ file disko-1.dd        
disko-1.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "mkfs.fat", 
Media descriptor 0xf8, sectors/track 32, heads 8, sectors 102400 
(volumes > 32 MB), FAT (32 bit), sectors/FAT 788, serial number 0x241a4420, 
unlabeled
```

**Key Information:**
- **File Type:** DOS/MBR boot sector
- **Filesystem:** FAT32
- **Size:** 102,400 sectors (approximately 50 MB for standard 512-byte sectors)
- **File System ID:** mkfs.fat (created with FAT filesystem utilities)
- **Serial Number:** 0x241a4420

### 2. Understanding the Hint

The challenge hint explicitly suggests using the `strings` command:
> "Maybe Strings could help? If only there was a way to do that?"

The `strings` command extracts printable character sequences from binary files, making it perfect for finding text data embedded in disk images.

## Solution

### String Extraction and Flag Search

Following the hint, we use `strings` to extract all readable text from the disk image and filter for the flag format:

```bash
$ strings disko-1.dd | grep "picoCTF"
picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}
```

**Command Breakdown:**
- `strings disko-1.dd` - Extracts all printable strings from the disk image
- `|` - Pipes the output to the next command
- `grep "picoCTF"` - Filters for lines containing "picoCTF"

## Flag

**`picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}`**

The flag itself hints at the solution method: "it's just a string" (written in leetspeak: `1t5_ju5t_4_5tr1n9`).

## Key Takeaways

### Forensics Fundamentals

1. **String Extraction**: The `strings` command is one of the most fundamental forensics tools
2. **Binary Analysis**: Not all data in binary files needs complex tools - sometimes simple text extraction works
3. **File Identification**: Always start by identifying the file type using `file` command

### The `strings` Command

**Basic Usage:**
```bash
strings [options] filename
```

**Common Options:**
- `-n <num>` - Set minimum string length (default is 4)
- `-e <encoding>` - Select character encoding
- `-a` - Scan entire file (default scans only data sections)

**Example:**
```bash
# Extract strings with minimum length of 10 characters
strings -n 10 disko-1.dd

# Search for specific patterns
strings disko-1.dd | grep -i "password"
strings disko-1.dd | grep -E "[0-9]{3}-[0-9]{2}-[0-9]{4}"
```

### Alternative Approaches

While `strings` solved this challenge, here are other methods that could work for disk image analysis:

#### 1. Mounting the Disk Image
```bash
# Create mount point
mkdir /mnt/disk

# Mount the disk image
sudo mount -o loop,ro disko-1.dd /mnt/disk

# Explore filesystem
ls -la /mnt/disk
cat /mnt/disk/somefile.txt

# Unmount when done
sudo umount /mnt/disk
```

#### 2. Using Autopsy/Sleuth Kit
```bash
# List filesystem information
mmls disko-1.dd

# List files in filesystem
fls -r disko-1.dd

# Extract specific file
icat disko-1.dd [inode] > extracted_file
```

#### 3. Hex Analysis
```bash
# View hex dump
xxd disko-1.dd | less

# Search for specific hex patterns
xxd disko-1.dd | grep "7069636F"  # "pico" in hex
```

## Tools Used

- `file` - File type identification
- `strings` - String extraction from binary files
- `grep` - Pattern matching and filtering

## Difficulty Assessment

**Difficulty:** ⭐☆☆☆☆ (Beginner)

This challenge is an excellent introduction to forensics because:
- It teaches the fundamental `strings` command
- It demonstrates that not all forensics requires complex tools
- The hint guides users toward the solution
- The flag format makes searching straightforward

## Related Commands

For future forensics challenges, here are related useful commands:

```bash
# Extract strings with context
strings -n 6 file.dd | grep -B 2 -A 2 "flag"

# Case-insensitive search
strings file.dd | grep -i "password"

# Output with file offsets
strings -t d file.dd | grep "picoCTF"

# Search for specific patterns
strings file.dd | grep -E "picoCTF\{[a-z0-9_]+\}"
```

## Challenge Naming

The challenge name "DISKO 1" is a play on words:
- **DISKO** = DISK + O (likely referring to disk I/O or disk operations)
- The "1" suggests this is part of a series with increasing difficulty

The flag text `1t5_ju5t_4_5tr1n9` (leetspeak for "it's just a string") confirms that this challenge is intentionally straightforward to introduce forensics concepts.
