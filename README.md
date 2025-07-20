# SimplePasswordCracker_Python

This is a simple educational password cracker built in Python using Tkinter.  
You can use it to test how fast weak passwords can be cracked based on hashes (MD5, SHA1, SHA256).
 
---

## 🚀 Features

- Hash any password instantly using SHA256, SHA1, or MD5
- Crack hashed passwords using a dictionary attack
- Live countdown timer based on password length
- Cracking log panel that shows every guess
- Fun surprise button 😎
- Sound effect when password is cracked
- Dark mode for better aesthetics
- Loads dictionary from `passwords.txt` (if it exists)

---

## 🛠 How it Works

1. Enter a hashed password (or hash one from the input field).
2. Select the hash method you used (SHA256 recommended).
3. Enter the **expected length** of the original password.
4. Click **Start Cracking**.
5. Watch the log as it tries each guess.
6. A success sound and result will show up if it's found before time runs out.

---

## 📂 File Structure

📁 project/
│
├── passwords.txt # Your custom dictionary (one password per line)
├── cracker.py # Main application (this file)
└── README.md # You're reading this

yaml
Copy
Edit

---

## 🧪 Educational Use Only

This tool is meant for **learning how hashing and cracking works**.  
Please don't use it to attack real systems or steal passwords. Be cool 😎.

---

Made with 🍵 + Python for cybersecurity beginners.

Made in 16/07/2025
 
