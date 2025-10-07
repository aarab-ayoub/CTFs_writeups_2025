# CTF Writeups Collection

This repository contains writeups for various Capture The Flag (CTF) challenges I've solved. Each writeup includes detailed explanations of the methodology, tools used, and key learning points.

---

## 📋 Table of Contents

- [HackTheBox - Forensics](https://app.hackthebox.com/challenges?category=7&sort_type=asc)
- [Suspicious Threat](https://app.hackthebox.com/challenges/Suspicious%2520Threat)

---

## HackTheBox - Forensics

### Suspicious Threat

**Difficulty:** Easy
**Category:** Forensics

#### Challenge Description

Our SSH server is showing strange library linking errors, and critical folders seem to be missing despite their confirmed existence. Investigate the anomalies in the library loading process and filesystem. Look for hidden manipulations that could indicate a userland rootkit.

**Credentials:** `root:hackthebox`

#### Solution

After logging in via SSH, I began investigating the system for signs of compromise. The first step was checking if standard binaries were behaving normally.

**Step 1: Identifying the Rootkit**

I used `ldd` to inspect the shared library dependencies of a common binary:

```bash
ldd /bin/ls
```

The output revealed a suspicious library:
```
/lib/x86_64-linux-gnu/libc.hook.so.6
```

The name `libc.hook.so.6` immediately indicated library injection, as legitimate system libraries don't contain "hook" in their names.

**Step 2: Verifying the Preload Mechanism**

To understand how this malicious library was being loaded globally, I checked the dynamic linker's preload configuration:

```bash
cat /etc/ld.so.preload
```

Output:
```
/lib/x86_64-linux-gnu/libc.hook.so.6
```

This confirmed the presence of a userland rootkit using `/etc/ld.so.preload` to inject itself into every running process on the system.

**Step 3: Neutralizing the Rootkit**

To disable the rootkit and restore normal system behavior, I moved the malicious library:

```bash
mv /lib/x86_64-linux-gnu/libc.hook.so.6 /tmp/
```

This breaks the preload chain, causing binaries to revert to legitimate system libraries.

**Step 4: Revealing Hidden Files**

With the rootkit disabled, I re-examined the filesystem:

```bash
ls -la /var
```

A previously hidden directory was now visible:
```
/var/pr3l04d_
```

**Step 5: Capturing the Flag**

```bash
cat /var/pr3l04d_/flag.txt
```

**Flag:** `HTB{...}`

#### Technical Analysis

This challenge demonstrated a classic userland rootkit technique:

- **LD_PRELOAD Injection:** The rootkit used `/etc/ld.so.preload` to force the dynamic linker to load its malicious library before all others
- **Function Hooking:** The malicious library intercepted standard libc functions like `readdir()`, `stat()`, and `open()` to hide specific files and directories
- **Userland Evasion:** By operating entirely in userspace, the rootkit avoided kernel-level detection mechanisms

#### Key Takeaways

- Always check `/etc/ld.so.preload` when investigating suspicious system behavior
- Use `ldd` to inspect binary dependencies for unexpected libraries
- Userland rootkits can effectively hide files without kernel access
- Moving or removing preloaded libraries can reveal hidden content

#### Tools Used

- `ldd` - List dynamic dependencies
- `ls` - List directory contents
- `cat` - View file contents
- `mv` - Move files

---

## Author

$ubZ3r0

## License

This repository is for educational purposes only.d
