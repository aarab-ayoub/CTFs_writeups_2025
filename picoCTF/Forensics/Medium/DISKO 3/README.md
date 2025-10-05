# DISKO 3 Challenge Writeup

## Challenge Overview

**Challenge Name:** DISKO 3  
**Category:** Forensics  
**Description:** Can you find the flag in this disk image? This time, its not as plain as you think it is! Download the disk image here.  
**Hint:** How will you search and extract files in a partition?

## Files Provided

- `disko-3.dd` - Disk image file

## Analysis

### 1. File Type Identification

First, identify the disk image structure:

```bash
$ file disko-3.dd        
disko-3.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "mkfs.fat", 
Media descriptor 0xf8, sectors/track 32, heads 8, sectors 204800 
(volumes > 32 MB), FAT (32 bit), sectors/FAT 1576, serial number 0x49838d0b, 
unlabeled
```

**Key Information:**
- **Filesystem:** FAT32
- **Size:** 204,800 sectors (≈100 MB)

### 2. Partition Table Analysis

Check the partition structure:

```bash
$ fdisk -l disko-3.dd 
Disk disko-3.dd: 100 MiB, 104857600 bytes, 204800 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000
```

This is a single FAT32 filesystem without multiple partitions.

## Solution

### Step 1: Mount the Disk Image

Mount the disk image to access its filesystem:

```bash
$ sudo mkdir -p /mnt/disk
$ sudo mount -o loop disko-3.dd /mnt/disk
```

### Step 2: Navigate to the Log Directory

After mounting, explore the filesystem and navigate to the log directory:

```bash
$ cd /mnt/disk/log
$ ls -la
total 1612
drwxr-xr-x 11 root root   3584 Mar 31  2025 .
drwxr-xr-x  3 root root    512 Jan  1  1970 ..
-rwxr-xr-x  1 root root  21322 Mar 31  2025 Xorg.0.log
-rwxr-xr-x  1 root root  20753 Mar 31  2025 Xorg.0.log.old
-rwxr-xr-x  1 root root      0 Mar 31  2025 alternatives.log
-rwxr-xr-x  1 root root    194 Mar 31  2025 alternatives.log.2.gz
drwxr-xr-x  2 root root   1536 Mar 31  2025 apt
-rwxr-xr-x  1 root root      0 Mar 31  2025 boot.log
-rwxr-xr-x  1 root root   7563 Mar 31  2025 boot.log.1
-rwxr-xr-x  1 root root   7125 Mar 31  2025 boot.log.5
-rwxr-xr-x  1 root root   7420 Mar 31  2025 boot.log.6
-rwxr-xr-x  1 root root 299509 Mar 31  2025 daemon.log
-rwxr-xr-x  1 root root  24374 Mar 31  2025 debug
-rwxr-xr-x  1 root root   3378 Mar 31  2025 dpkg.log.1
-rwxr-xr-x  1 root root      0 Mar 31  2025 dpkg.log.2.gz
-rwxr-xr-x  1 root root 161557 Mar 31  2025 dpkg.log.4.gz
-rwxr-xr-x  1 root root 259660 Mar 31  2025 dpkg.log.5.gz
-rwxr-xr-x  1 root root  32032 Mar 31  2025 faillog
-rwxr-xr-x  1 root root     78 Jul 17 16:06 flag.gz
drwxr-xr-x  3 root root    512 Mar 31  2025 inetsim
drwxr-xr-x  3 root root   1024 Mar 31  2025 installer
drwxr-xr-x  3 root root    512 Mar 31  2025 journal
-rwxr-xr-x  1 root root  18801 Mar 31  2025 kern.log.3.gz
-rwxr-xr-x  1 root root  18671 Mar 31  2025 kern.log.4.gz
-rwxr-xr-x  1 root root 292292 Mar 31  2025 lastlog
drwxr-xr-x  2 root root   1024 Mar 31  2025 lightdm
-rwxr-xr-x  1 root root     59 Mar 31  2025 macchanger.log.4.gz
drwxr-xr-x  2 root root    512 Mar 31  2025 mysql
drwxr-xr-x  2 root root    512 Mar 31  2025 private
drwxr-xr-x  2 root root    512 Mar 31  2025 stunnel4
-rwxr-xr-x  1 root root  46637 Mar 31  2025 syslog.3.gz
-rwxr-xr-x  1 root root 288914 Mar 31  2025 syslog.4.gz
drwxr-xr-x  2 root root    512 Mar 31  2025 sysstat
-rwxr-xr-x  1 root root    195 Mar 31  2025 vmware-network.1.log
-rwxr-xr-x  1 root root    195 Mar 31  2025 vmware-network.2.log
-rwxr-xr-x  1 root root    195 Mar 31  2025 vmware-network.3.log
-rwxr-xr-x  1 root root    195 Mar 31  2025 vmware-network.4.log
-rwxr-xr-x  1 root root    193 Mar 31  2025 vmware-network.5.log
-rwxr-xr-x  1 root root    193 Mar 31  2025 vmware-network.6.log
-rwxr-xr-x  1 root root    195 Mar 31  2025 vmware-network.7.log
-rwxr-xr-x  1 root root    195 Mar 31  2025 vmware-network.8.log
-rwxr-xr-x  1 root root      0 Mar 31  2025 vmware-network.log
-rwxr-xr-x  1 root root   3007 Mar 31  2025 vmware-vmsvc-root.1.log
-rwxr-xr-x  1 root root   3135 Mar 31  2025 vmware-vmsvc-root.2.log
-rwxr-xr-x  1 root root   3304 Mar 31  2025 vmware-vmsvc-root.3.log
-rwxr-xr-x  1 root root   2292 Mar 31  2025 vmware-vmsvc-root.log
-rwxr-xr-x  1 root root  19624 Mar 31  2025 vmware-vmtoolsd-root.log
-rwxr-xr-x  1 root root  87168 Mar 31  2025 wtmp
```

**Key Finding:** `flag.gz` - A compressed file of only 78 bytes!

### Step 3: Extract the Compressed File

Copy the flag file outside the mounted disk:

```bash
$ cp flag.gz ~/Downloads/
$ cd ~/Downloads/
```

### Step 4: Decompress the File

Decompress the gzip file:

```bash
$ gunzip flag.gz
```

This creates a file named `flag`.

### Step 5: Read the Flag

```bash
$ cat flag
Here is your flag
picoCTF{n3v3r_z1p_2_h1d3_26d4f233}
```

## Flag

**`picoCTF{n3v3r_z1p_2_h1d3_26d4f233}`**

## Key Takeaways

1. **Filesystem Navigation**: Unlike previous challenges, this required mounting the disk image and navigating its directory structure
2. **File Extraction**: The flag was stored in a compressed file, requiring proper extraction and decompression
3. **Compression Handling**: Understanding gzip compression and how to decompress files with `gunzip`
4. **Realistic Forensics**: The flag was hidden in a log directory among many other log files, simulating real-world forensics scenarios

## Tools Used

- `file` - File type identification
- `fdisk` - Partition analysis
- `mount` - Filesystem mounting
- `ls` - Directory listing
- `cp` - File copying
- `gunzip` - Gzip decompression
- `cat` - File reading
