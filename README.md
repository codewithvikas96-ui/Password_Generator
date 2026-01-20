# 🔐 Advanced Password Generator Suite

This repository contains two secure password generators written in **Python**:

1. **CLI Version (`cli/password_cli.py`)**  
   A simple, interactive command‑line tool for generating random passwords.

2. **GUI Version (`gui/password_gui.py`)**  
   A modern PyQt5 desktop application with a sleek interface, exclusion options, and clipboard support.

---

## 🚀 Features

- Cryptographically secure randomness (`secrets` module)
- Customizable length (8–64 characters)
- Include/exclude:
  - **Uppercase letters (A–Z)**
  - **Lowercase letters (a–z)**
  - **Digits (0–9)**
  - **Symbols (!@#$...)**
- Exclude specific characters (GUI only)
- One‑click copy to clipboard (GUI only)
- Password strength validation (length vs. rules)

---

## 📂 Project Structure
```bash
password-generator/
├── .venv
├── README.md
├── requirements.txt
├── cli/
│   └── password_cli.py
└── gui/
└── password_gui.py

```
---

## ▶️ Usage

**CLI Version**
Run the command‑line tool:
```bash
python cli/password_cli.py
```
- You’ll be prompted to:
- Enter password length (≥ 8)
- Choose whether to include uppercase, lowercase, digits, and symbols
- Generate multiple variations until satisfied

**GUI Version**
__Run the PyQt5 application:__
```bash
python gui/password_gui.py
```

Features:
- Spinbox to set password length
- Checkboxes for character types
- Exclusion field (e.g., exclude O0l1)
- Generate button with styled output
- Copy to clipboard button

---

