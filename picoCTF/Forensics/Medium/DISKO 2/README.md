# DISKO 2 Challenge Writeup

## Challenge Overview

**Challenge Name:** DISKO 2  
**Category:** Forensics  
**Description:** Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone! Download the disk image here.  
**Hint:** How can you extract/isolate a partition?

This challenge builds upon DISKO 1 by introducing multi-partition disk images and requiring partition isolation to find the correct flag.

## Files Provided

- `disko-2.dd` - Multi-partition disk image file

## Analysis

### 1. File Type Identification

First, identify the disk image structure:

```bash
$ file disko-2.dd        
disko-2.dd: DOS/MBR boot sector; partition 1 : ID=0x83, start-CHS (0x0,32,33), 
end-CHS (0x3,80,13), startsector 2048, 51200 sectors; partition 2 : ID=0xb, 
start-CHS (0x3,80,14), end-CHS (0x7,100,29), startsector 53248, 65536 sectors
```

**Key Observations:**
- Multiple partitions detected (2 partitions)
- **Partition 1:** ID=0x83 (Linux filesystem), starts at sector 2048
- **Partition 2:** ID=0xb (W95 FAT32), starts at sector 53248

### 2. Partition Layout Analysis

Use `fdisk` to get detailed partition information:

```bash
$ fdisk -l disko-2.dd    
Disk disko-2.dd: 100 MiB, 104857600 bytes, 204800 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x8ef8eaee

Device      Boot Start    End Sectors Size Id Type
disko-2.dd1       2048  53247   51200  25M 83 Linux
disko-2.dd2      53248 118783   65536  32M  b W95 FAT32
```

**Partition Details:**

| Partition | Start Sector | End Sector | Size (Sectors) | Size (MB) | Type | Filesystem |
|-----------|--------------|------------|----------------|-----------|------|------------|
| disko-2.dd1 | 2048 | 53247 | 51200 | 25M | 0x83 | Linux |
| disko-2.dd2 | 53248 | 118783 | 65536 | 32M | 0xb | W95 FAT32 |

### 3. The Problem: Multiple Fake Flags

The challenge description mentions "The right one is Linux!" which is a crucial hint. Let's see what happens if we search the entire disk:

```bash
$ strings disko-2.dd | grep "picoCTF"
picoCTF{fake_flag_1_abc123}
picoCTF{fake_flag_2_def456}
picoCTF{fake_flag_3_ghi789}
picoCTF{4_P4Rt_1t_i5_a93c3ba0}
picoCTF{fake_flag_4_jkl012}
...
```

**Result:** Multiple flags appear, making it impossible to determine the correct one without additional analysis.

## Solution

### Step 1: Extract the Linux Partition

The challenge hint and description point us to the Linux partition. We need to isolate it using the `dd` command:

```bash
$ dd if=disko-2.dd of=Linux.img bs=512 skip=2048 count=51200
51200+0 records in
51200+0 records out
26214400 bytes (26 MB, 25 MiB) copied
```

**Command Breakdown:**
- `if=disko-2.dd` - Input file (source disk image)
- `of=Linux.img` - Output file (extracted partition)
- `bs=512` - Block size (512 bytes = sector size)
- `skip=2048` - Skip first 2048 sectors (start of Linux partition)
- `count=51200` - Read 51200 sectors (size of Linux partition)

**Calculation:**
```
Start: 2048 sectors × 512 bytes/sector = 1,048,576 bytes (1 MB offset)
Size: 51200 sectors × 512 bytes/sector = 26,214,400 bytes (25 MB)
```

### Step 2: Search the Isolated Partition

Now search for the flag in the extracted Linux partition:

```bash
$ strings Linux.img | grep "picoCTF"
picoCTF{4_P4Rt_1t_i5_a93c3ba0}
```

**Result:** Only one flag appears in the Linux partition - this is the correct flag!

## Flag

**`picoCTF{4_P4Rt_1t_i5_a93c3ba0}`**

The flag text `4_P4Rt_1t_i5` (leetspeak for "a part it is") refers to the solution method of isolating a specific partition.

## Key Takeaways

### Forensics Concepts

1. **Partition Tables**: Understanding how disk partitions are organized and addressed
2. **Partition Isolation**: Extracting specific partitions from multi-partition disk images
3. **Data Hiding**: Adversaries can hide data across multiple partitions as a decoy technique
4. **Targeted Analysis**: Analyzing specific partitions rather than the entire disk saves time

### The `dd` Command

The `dd` (data duplicator) command is essential for disk forensics:

**Basic Syntax:**
```bash
dd if=<input> of=<output> bs=<blocksize> skip=<blocks> count=<blocks>
```

**Common Forensics Uses:**

```bash
# Extract a partition (as in this challenge)
dd if=disk.dd of=partition.img bs=512 skip=2048 count=51200

# Create disk image from physical drive
dd if=/dev/sda of=disk.img bs=4M status=progress

# Extract specific bytes from file
dd if=file.bin of=extracted.bin bs=1 skip=1024 count=2048

# Wipe a disk securely
dd if=/dev/zero of=/dev/sdb bs=4M status=progress
```

### Partition Type IDs

Common partition type identifiers:

| ID | Type | Description |
|----|------|-------------|
| 0x83 | Linux | Linux native filesystem (ext2/3/4) |
| 0x82 | Linux swap | Linux swap partition |
| 0xb | W95 FAT32 | Windows 95 FAT32 |
| 0x7 | NTFS | Windows NT filesystem |
| 0xc | W95 FAT32 (LBA) | FAT32 with LBA |
| 0x5 | Extended | Extended partition |

## Alternative Methods

### Method 1: Mount the Partition Directly

```bash
# Calculate offset: 2048 sectors × 512 bytes = 1048576 bytes
sudo mkdir /mnt/linux_part
sudo mount -o loop,offset=1048576,ro disko-2.dd /mnt/linux_part

# Search for flag
grep -r "picoCTF" /mnt/linux_part/

# Unmount
sudo umount /mnt/linux_part
```

### Method 2: Using losetup

```bash
# Set up loop device with partition
sudo losetup -fP disko-2.dd
# This creates /dev/loop0p1 and /dev/loop0p2

# Mount the Linux partition
sudo mount -o ro /dev/loop0p1 /mnt/linux_part

# Search
grep -r "picoCTF" /mnt/linux_part/

# Cleanup
sudo umount /mnt/linux_part
sudo losetup -d /dev/loop0
```

### Method 3: Using mmls and dd

```bash
# List partitions with Sleuth Kit
mmls disko-2.dd

# Extract based on output
dd if=disko-2.dd of=linux.img bs=512 skip=<start_sector> count=<length>
```

### Method 4: Automated Extraction with binwalk

```bash
# Extract all filesystems automatically
binwalk -e disko-2.dd

# Search in extracted files
grep -r "picoCTF" _disko-2.dd.extracted/
```

## Challenge Progression

This challenge builds on DISKO 1 by adding complexity:

| Aspect | DISKO 1 | DISKO 2 |
|--------|---------|---------|
| Partitions | Single partition | Multiple partitions |
| Flags | One flag | Multiple decoy flags |
| Difficulty | Simple `strings` | Partition isolation required |
| Skills | Basic string extraction | Partition analysis, dd usage |

## Tools Used

- `file` - File type identification
- `fdisk` - Partition table analysis
- `dd` - Partition extraction
- `strings` - String extraction
- `grep` - Pattern matching

## Tips for Similar Challenges

1. **Always analyze partition structure first** using `fdisk`, `mmls`, or `parted`
2. **Read challenge descriptions carefully** - "The right one is Linux!" was a critical hint
3. **Isolate partitions** when dealing with multi-partition images to avoid confusion
4. **Calculate offsets correctly** - Use sector size (usually 512 bytes) × start sector
5. **Consider mounting** as an alternative to extraction for filesystem exploration

## Difficulty Assessment

**Difficulty:** ⭐⭐☆☆☆ (Beginner-Intermediate)

This challenge introduces:
- Multi-partition disk images
- The `dd` command for partition extraction
- Decoy data to mislead simple analysis
- Practical forensics workflow

## Security Implications

This challenge demonstrates a real-world anti-forensics technique:
- **Data Hiding**: Spreading decoy data across multiple partitions
- **Misdirection**: Making superficial analysis yield incorrect results
- **Partition Manipulation**: Using different filesystem types to complicate analysis

Forensics analysts must be thorough and methodical to avoid being misled by such techniques.
