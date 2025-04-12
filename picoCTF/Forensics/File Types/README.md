# CTF Challenge: Flag.pdf Extraction

## Challenge Description
We are given a file named Flag.pdf, but it's not actually a PDF. This challenge requires navigating through multiple layers of compression to find the hidden flag.

## Solution

### Initial Analysis
We are given the file Flag.pdf. I tried to open this up in my PDF reader, but it said that it cannot be opened.

So I checked the file type using,
```
$ file Flag.pdf
```
And this revealed that it was a `shell archive text`

The contents inside were a shell archive script that when executed would extract another file.

### Extracting the Shell Archive
So I copied this file into a file with a .sh extension,
```
$ cp Flag.pdf Flag.sh
```
And added the execution permission,
```
$ chmod +x Flag.sh
```
And executed this script,
```
$ ./Flag.sh
```

After executing, a file called `flag` was generated, and checking the file type revealed that it was a `current ar archive`.

### Navigating Through Multiple Compression Layers
Then I used `binwalk` to extract the ar archive,
```
$ binwalk -e flag
```
Which created a new folder called `_flag.extracted`, and inside was a file called `64`.

I checked the file type of `64`, and revealed that it was a `gzip compressed data`

I used `binwalk` to extract the gzip,
```
$ binwalk -e 64
```
The extracted folder contained a file called `flag`,

I checked the file type of `flag`, and revealed that it was a `lzip compressed data`. Using `binwalk` did not extract it, so I extracted this using,
```
$ lzip -d -k flag
```

This created a file called `flag.out`, and revealed that it was a `LZ4 compressed data`. So I extracted it using,
```
$ lz4 -d flag.out flag2.out
```

This created a file called `flag2.out`, and revealed that it was a `LZMA compressed data`. So I extracted it using,
```
$ lzma -d -k flag2.out
```
However, this returned `Filename has an unknown suffix, skipping`, so I renamed it to flag2.lzma and I extracted it using,
```
$ lzma -d -k flag2.lzma
```

This created a file called `flag2`, and revealed that it was a `LZOP compressed data`. Like last time, it gave `unknown suffix`, so I renamed it to `flag2.lzop`, and I extracted it using,
```
$ lzop -d -k flag2.lzop -o flag3
```

This created a file called `flag3`, and revealed that it was a `LZIP compressed data`. So I extracted it using,
```
$ lzip -d -k flag3
```

This created a file called `flag3.out`, and revealed that it was a `XZ compressed data`. I renamed it to `flag4.xz` and I extracted it using,
```
$ xz -d -k flag4.xz
```

### Finding the Flag
This created a file called `flag4`, and revealed that it was a `ASCII text` and contained the following:

```
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f37396230316332367d0a
```

Converting this hex string to ASCII:

```
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}
```

And there's our flag!

## Conclusion
This challenge demonstrated the use of various file compression techniques stacked on top of each other to obfuscate data. It required knowledge of different compression formats and their corresponding extraction tools to navigate through each layer.
