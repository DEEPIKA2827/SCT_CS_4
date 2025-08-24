# SCT_CS_4
Safe Python Keylogger Simulator for learning real-time input handling and file logging (Task 4 - SCT_CS Internship)
# SCT_CS_4 - Python Keylogger Simulator

## Overview
This repository contains a **Python Keylogger Simulator**, developed as part of **Task 4 for the SCT_CS Software Engineering Internship**.  

The project is purely for **educational purposes** to demonstrate **real-time input handling** and **file logging** in Python using the `pynput` library. It captures keystrokes typed **inside the program**, displays them **live in the terminal**, and logs them to a file (`key_log.txt`).  

**⚠️ Important:** This project is **not for malicious use**. It is intended for learning and experimentation on your own machine only.

---

## Features
- Captures normal alphanumeric keys
- Detects and logs special keys (Enter, Space, Shift, etc.)
- Displays live output in terminal
- Saves keystrokes to `key_log.txt`
- Press **ESC** to stop logging safely

---

## Requirements
- Python 3.x
- `pynput` library  
Install via pip:
```bash
pip install pynput
