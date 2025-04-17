## Challenge Name: verify

**Category**: Forensics  
**Points**: –  

### Description
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

```
ssh -p 56770 ctf-player@rhea.picoctf.net
```

Use the password: `84b12bae`  
Accept the fingerprint with `yes`, and run `ls` once connected to begin.

Checksum to verify:  
`3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4`

To decrypt a file once you've verified the hash, run:  
```
./decrypt.sh files/<file>
```

---

### 🧠 Hints
- Checksums let you verify that a file is unmodified and authentic.
- Use `sha256sum <file>` to get a file's checksum.
- You can compute hashes for all files in a directory using:
  ```
  sha256sum files/*
  ```
- Use `grep` to find the correct file by matching the hash:
  ```
  sha256sum files/* | grep 3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4
  ```

---

### ✅ Solution

We're given a SHA-256 hash:
```
3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4
```

We want to find which file inside the `files/` directory matches this hash. So we compute the hashes for all files and grep for the one that matches:

```bash
ctf-player@pico-chall$ sha256sum files/* | grep 3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4
3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4  files/e018b574
```

Now that we've identified the correct file (`files/e018b574`), we can decrypt it using the provided script:

```bash
ctf-player@pico-chall$ ./decrypt.sh files/e018b574
```

And the output is:

```
picoCTF{trust_but_verify_e018b574}
```

---

### 🏁 Flag

```
picoCTF{trust_but_verify_e018b574}
```
