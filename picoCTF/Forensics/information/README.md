# 🕵️‍♂️ picoCTF - Forensics Challenge: "information"

## 📄 Description

> Files can always be changed in a secret way. Can you find the flag?  
> **File provided**: `cat.jpg`

---

## 🧠 Challenge Summary

This challenge hints at hidden or modified information within a seemingly normal image file. As the name and description suggest, it’s a classic case of **metadata manipulation**.

---

## 🔍 Solution

I suspected the flag might be hiding in the metadata of the image, so I used [`exiftool`](https://exiftool.org/) — a powerful utility for reading and editing metadata.

```bash
exiftool cat.jpg
```

### 📸 Key metadata fields revealed:

```text
Copyright Notice       : PicoCTF
License                : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                 : PicoCTF
```

The `License` field immediately stood out — it contained what looked like a **Base64-encoded** string:

```text
cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```

### 🔓 Decoding it:

```bash
echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
```

### 🎉 Output:

```
picoCTF{the_m3tadata_1s_modified}
```

---

## 🏁 Flag

```
picoCTF{the_m3tadata_1s_modified}
```

---

## 🧰 Tools Used

- [ExifTool](https://exiftool.org/)
- `base64` (CLI utility)

---

## ✍️ Author

Challenge write-up by **$ubZ3r0**
