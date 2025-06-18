# Task - 2
## 🖼️ Secure Image Encryption Tool

A Python-based tool that encrypts and decrypts images using **XOR encryption** with a pseudo-random key derived from a user-defined numeric seed.

---

### 🔐 Features

* Encrypts any `.png`, `.jpg`, or `.jpeg` image using XOR and a numeric key
* Decrypts using the **same** key to recover the original image
* Compares original and decrypted images to verify accuracy
* Uses `numpy` and `PIL` for efficient image processing

---

### 🛠️ Requirements

* Python 3.x
* Install required packages:

  ```bash
  pip install pillow numpy
  ```

---

### 🚀 How to Use

1. **Run the script:**

   ```bash
  Image Encryption Tool.py
   ```

2. **Choose an option:**

   * `e` – Encrypt an image
   * `d` – Decrypt an image
   * `c` – Compare original and decrypted images
   * `q` – Quit

3. **Follow the prompts**, entering:

   * A valid numeric key (same for encryption & decryption)
   * Image path(s)

---

### 📁 Output Files

* Encrypted image → `encrypted_image.png`
* Decrypted image → `decrypted_image.png`

---

### 📋 Example

```
🔐 Welcome to the Sreeram's Secure Image Encryption Tool

Choose an option:
  e - Encrypt an image
  d - Decrypt an image
  c - Compare original and decrypted image
  q - Quit the program

Your choice: e
Enter a numeric encryption key: 12345
Enter the path to the image: photo.png
✅ Encrypted image saved as: encrypted_image.png
```

---

### ⚠️ Notes

* You **must use the same numeric key** for encryption and decryption.
* XOR encryption is **not secure for sensitive data**, but useful for learning and lightweight obfuscation.

---
