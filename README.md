# GUI-Based Audio Integrity Checking Application

## Overview
This project is a **GUI-based Audio Integrity Checking Application** developed as part of a **Cybersecurity** project. It ensures that an audio file has not been tampered with by verifying its **cryptographic hash (SHA-256)** against a stored database. The system also generates **audio fingerprints, metadata analysis, and spectrogram visualization** to check for any integrity violations. Additionally, a **PDF integrity report** is generated.

---

## Features
- **GUI Interface:** Simple and user-friendly PyQt6 interface for file selection.
- **Cryptographic Hashing:** Uses SHA-256 to generate and store hashes for verification.
- **Audio Fingerprinting:** Checks for any unauthorized modifications.
- **Spectrogram Analysis:** Visualizes audio characteristics using Mel spectrograms.
- **Metadata Extraction:** Retrieves bit rate, sample rate, and audio channels.
- **Database Storage:** Stores file hashes in a **MySQL database** for future comparison.

---

## Installation Guide

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/your-repo/audio-integrity-checker.git
cd audio-integrity-checker
```

### **Step 2: Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Step 3: Run the Application**
```sh
python main.py
```

---

## Project Structure

```sh
audio_integrity_checker/
│── main.py                  # Main script to run the GUI
│── requirements.txt          # Dependencies
│── gui.py                    # GUI implementation using PyQt
│── audio_processing.py       # Handles hashing, fingerprinting, and spectrogram generation
│── reports.py                # Generates integrity reports
│── database.py               # Manages hash storage for verification
│── fingerprints/             # Stores fingerprints for verification
│── reports/                  # Stores generated integrity reports
│── samples/                  # Sample audio files for testing
```

---

## How It Works

1. **User selects an audio file** through the GUI.
2. **SHA-256 hash is generated** and compared with the stored hash in the MySQL database.
3. **If the hash matches**, the file is verified as **authentic**.
4. **If the hash differs**, the file may have been **tampered with**.
5. **A spectrogram is displayed** to visualize audio characteristics.

---

## NOTES

- **Before verifying integrity**, the user must store the original hash first.
- If the file is moved, renamed, or modified, its hash will **not match** the stored hash.
- The app does not detect **what changes were made**—only whether the file was modified.