### **1. DFIR (Digital Forensics & Incident Response)**
**Challenge 1: Corrupted Memory Dump (Hard)**   //DONE DONE 
- **Description**: Analyze a fake memory dump (`corrupted_dump_v2.bin`) with fragmented flag parts (AES, Base64, Zlib).  
- **Skills**: Memory analysis, encryption, data carving.  
- **Hint**: "The key is in the memory itself. Look for 'AES_FLAG:' and 'B64:' markers."  

**Challenge 2: Disk Detective (Medium)**  //TODO
- **Description**: A disk image (`disk.img`) has a deleted file containing the flag.  
- **Skills**: File recovery (`photorec`, `fls`), partition analysis.  
- **Hint**: "Check the lost+found directory."  

**Challenge 3: Wireshark Traffic Analysis (Easy)** // TODO by n0rddin  


**Challenge 4: Ransomware Artifacts (Hard)**  //TODO
- **Description**: A ransomware-encrypted file (`secret.docx.enc`) and memory dump. Find the decryption key.  
- **Skills**: Volatility, ransomware analysis.  

---

### **2. MISC (Miscellaneous)**
**Challenge 1: Python Frequency Puzzle (Medium)** //DONE DONE 
- **Description**: Extract a flag from a WAV file (`secret.wav`) using FFT in Python.  
- **Skills**: Signal processing, Python scripting.  
- **Hint**: "Each character has its own frequency slot."  

**Challenge 2: Image Bit Manipulation (Easy)**  //TODO
- **Description**: A PNG image (`puzzle.png`) hides the flag in LSB (Least Significant Bits).  
- **Skills**: Steganography tools (`stegsolve`, `zsteg`).  
- **Hint**: "Use `zsteg` or Python PIL to check RGB values."  

**Challenge 3: Telegram Bot Flag (Medium)**  //IN PROGRESS
- **Description**: A Telegram bot (`@CTF_FlagBot`) gives the flag if you solve a math puzzle.  
- **Skills**: API interaction, automation.  
- **Hint**: "The bot responds to `/start` and `/solve <answer>`."  

**Challenge 4: STARS**  // DONE
- **Description**: "An amateur astronomer captured this starfield, but the patterns seem... intentional. What’s hidden in the void?".  


---

### **3. OSINT (Open-Source Intelligence)**
**Challenge 1: Blurred Website Screenshot (Medium)**   //TODO
- **Description**: A blurred screenshot of a darknet site (Ahmia) hides the URL. Find the original.  
- **Skills**: Reverse image search, darknet navigation.  
- **Hint**: "The site sells 'rare books'."  

<!-- **Challenge 2: Real Madrid Riddle (Easy)**  //TODO -->
<!-- - **Description**: "What is the name of Real Madrid’s stadium before 2023?" Flag: `MED{<answer>}`.   -->
<!-- - **Skills**: Quick Google search.   -->

**Challenge 3: "The Lost Expedition"** // DONE
- **Description: titanic. Format: MED{XX.XXXXXX,-XX.XXXXXX}."**

<!-- **Challenge 4: Twitter Clue (Medium)**  //TODO  by n0rrdin
- **Description**: A deleted tweet from `@CTF_HintMaster` contained the flag. Find it via archive.org.  
- **Skills**: Wayback Machine, tweet archiving.   -->


### **Bonus Challenges (Flexible Categories)**
- **DFIR**: "Log Analysis" (Apache logs with hidden flag).  
- **MISC**: "QR Chain" (Multiple QR codes leading to the flag).  
- **OSINT**: "Email Tracing" (Find the flag in a leaked email dump).  

---



