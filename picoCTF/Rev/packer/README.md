# Packer Challenge Writeup

## Challenge Overview
In this reverse engineering challenge called "packer", we were given a binary file. The hint suggested that we should look into techniques used to reduce the size of binaries after compilation.

## Initial Analysis
Based on the hint, I suspected that the binary might be compressed or "packed" using a packing utility. One of the most common packers is UPX (Ultimate Packer for eXecutables), so I decided to check if the binary was packed with UPX.

## Solution Steps

### Step 1: Check if the binary is packed with UPX
First, I used the UPX tool to list information about the binary:

```bash
$ upx -l out 
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.4       Markus Oberhumer, Laszlo Molnar & John Reiser    May 9th 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    872088 ->    336520   38.59%   linux/amd64   out
```

The output confirmed that the binary was indeed packed with UPX, with a compression ratio of 38.59%.

### Step 2: Unpack the binary
Next, I unpacked the binary using UPX with the `-d` flag:

```bash
$ upx -d out 
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.4       Markus Oberhumer, Laszlo Molnar & John Reiser    May 9th 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
[WARNING] bad b_info at 0x4b718

[WARNING] ... recovery at 0x4b714

    877724 <-    336520   38.34%   linux/amd64   out

Unpacked 1 file.
```

Despite some warnings during the unpacking process, the tool successfully unpacked the binary.

### Step 3: Analyze the unpacked binary
I then used a decompiler (Cutter with Ghidra decompiler) to analyze the unpacked binary. In the main function, I found the following interesting code:

```c
sym.puts("Password correct, please see flag: 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f33373161613966667d", 
         *(int64_t *)(puVar6 + 0x10));
```

### Step 4: Extract and decode the flag
The string in the `puts` function appeared to be a hexadecimal representation of the flag. Converting this hex string to ASCII revealed the flag:

```
7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f33373161613966667d
```

Decoding from hex to ASCII:

```
picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_371aa9ff}
```

## Conclusion
This challenge demonstrated the importance of understanding binary packing techniques in reverse engineering. By recognizing that the binary was packed with UPX, unpacking it, and then analyzing the decompiled code, we were able to find and decode the flag.

The flag itself, `picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_371aa9ff}`, cleverly references the technique used in the challenge - unpacking UPX binaries.
