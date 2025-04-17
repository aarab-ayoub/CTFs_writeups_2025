# 🕵️‍♂️ picoCTF - Forensics Challenge: "CanYouSee"

## 📄 Description

> How about some hide and seek?  
>  
> **Hints**:  
> - How can you view the information about the picture?  
> - If something isn't in the expected form, maybe it deserves attention?

**File provided**: `ukn_reality.jpg`

---

## 🧠 Challenge Summary

This challenge suggests something hidden in the image — likely in a subtle, non-visible way. The hint pushes us toward inspecting the metadata, which is a common vector in forensics-style challenges.

---

## 🔍 Solution

I used [`exiftool`](https://exiftool.org/) to inspect the image file’s metadata for any hidden clues:

```bash
exiftool ukn_reality.jpg
```

### 📸 Key metadata fields revealed:

```text
Attribution URL : cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==
```

This field clearly contains a **Base64-encoded** string. Let’s decode it.

### 🔓 Decoding it:

```bash
echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==" | base64 -d
```

### 🎉 Output:

```
picoCTF{ME74D47A_HIDD3N_6a9f5ac4}
```

---

## 🏁 Flag

```
picoCTF{ME74D47A_HIDD3N_6a9f5ac4}
```

---

## 🧰 Tools Used

- [ExifTool](https://exiftool.org/)
- `base64` (CLI utility)

---

## ✍️ Author

Challenge write-up by **your_name_here**
