# Mob Psycho - PicoCTF Challenge Writeup

## Challenge Information
- **Name**: Mob Psycho
- **Category**: Reverse Engineering / Mobile
- **Description**: Can you handle APKs? Download the android apk here.
- **Hints**: 
  1. Did you know you can `unzip` APK files?
  2. Now you have the whole host of shell tools for searching these files.

## Solution Overview

This challenge involves analyzing an Android APK file to find a hidden flag. The key insight is that APK files are essentially ZIP archives that can be extracted using standard tools.

## Step-by-Step Solution

### Step 1: Understanding APK Files
Android APK (Android Package) files are compressed archives similar to ZIP files. They contain all the resources, code, and assets needed to run an Android application.

### Step 2: Extract the APK
Since APK files are ZIP archives, we can extract them using the `unzip` command:

```bash
unzip [apk_filename].apk
```

This will extract all the contents of the APK into the current directory, revealing the application's file structure.

### Step 3: Search for Flag Files
After extraction, we need to locate files that might contain the flag. Using the `find` command to search for files with "flag" in their name:

```bash
find . -type f -name "flag*"
```

**Output:**
```
./res/color/flag.txt
```

This reveals a file named `flag.txt` in the `res/color/` directory.

### Step 4: Examine the Flag File
Reading the contents of the discovered file:

```bash
cat ./res/color/flag.txt
```

**Output:**
```
7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f37303364643965667d
```

The file contains what appears to be a hexadecimal string.

### Step 5: Decode the Hex String
The hex string needs to be decoded to reveal the actual flag. We can use various tools like `xxd`, `python`, or online hex decoders:

```bash
echo "7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f37303364643965667d" | xxd -r -p
```

**Result:**
```
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_703dd9ef}
```

## Key Concepts Learned

1. **APK Structure**: APK files are ZIP archives containing Android app resources
2. **File System Navigation**: Using `find` command to locate specific files
3. **Hex Decoding**: Converting hexadecimal strings back to ASCII text
4. **Mobile Reverse Engineering**: Basic techniques for analyzing mobile applications

## Tools Used
- `unzip` - For extracting APK contents
- `find` - For locating files within the extracted directory
- `cat` - For reading file contents
- `xxd` or hex decoder - For converting hex to ASCII

## Flag
```
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_703dd9ef}
```

## Alternative Approaches

1. **Using Android Studio**: Import the APK and browse resources through the IDE
2. **APK Analysis Tools**: Tools like `apktool` or `jadx` for more detailed analysis
3. **Manual Hex Decoding**: Using Python's `bytes.fromhex()` method
4. **Grep Search**: Using `grep -r "picoCTF"` to search for flag patterns across all files

## Conclusion

This challenge demonstrates basic mobile reverse engineering techniques and the importance of understanding file formats. The straightforward nature of the challenge emphasizes that sometimes the simplest approach (treating APK as ZIP) is the most effective solution.
