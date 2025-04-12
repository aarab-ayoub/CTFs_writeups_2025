CTF Challenge Writeup: Shell Archive Extraction
Challenge Overview
In this challenge, we're given a file named "Flag.pdf" that doesn't open as a normal PDF. Through a series of file extraction techniques, we need to recover the hidden flag.
Solution
The challenge starts with a seemingly innocent PDF file that won't open properly. Let's investigate step by step:
Initial Analysis
When attempting to open Flag.pdf, it fails to load in a PDF reader. This suggests it might not actually be a PDF file.
bash$ file Flag.pdf
Flag.pdf: shell archive text
Interesting! This isn't a PDF at all, but rather a shell archive - a self-extracting script.
Extracting the Shell Archive
I copied the file to a shell script and executed it:
bash$ cp Flag.pdf Flag.sh
$ chmod +x Flag.sh
$ ./Flag.sh
After execution, a new file called flag was generated.
Working Through Multiple Compression Layers
Checking the file type revealed our extraction journey had just begun:
bash$ file flag
flag: current ar archive
Using binwalk to extract the archive:
bash$ binwalk -e flag
This created a folder _flag.extracted containing a file named 64, which was a gzip compressed file.
I continued extracting through multiple compression layers:

Extract gzip file:
bash$ binwalk -e 64
This created a file called flag (lzip compressed data)
Extract lzip file:
bash$ lzip -d -k flag
This created flag.out (LZ4 compressed data)
Extract LZ4 file:
bash$ lz4 -d flag.out flag2.out
This created flag2.out (LZMA compressed data)
Extract LZMA file (after renaming):
bash$ mv flag2.out flag2.lzma
$ lzma -d -k flag2.lzma
This created flag2 (LZOP compressed data)
Extract LZOP file (after renaming):
bash$ mv flag2 flag2.lzop
$ lzop -d -k flag2.lzop -o flag3
This created flag3 (LZIP compressed data)
Extract LZIP file:
bash$ lzip -d -k flag3
This created flag3.out (XZ compressed data)
Extract XZ file (after renaming):
bash$ mv flag3.out flag4.xz
$ xz -d -k flag4.xz


Finding the Flag
Finally, flag4 was created - an ASCII text file containing the following hex string:
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f37396230316332367d0a
Converting from hex to ASCII:
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}
And there we have our flag!
Conclusion
This challenge demonstrates a technique called "matryoshka" - nesting multiple compression formats within each other to hide data. It required knowledge of various file formats and their corresponding extraction tools.
The key lesson: never trust file extensions! Always verify the actual file type with tools like file before proceeding.
