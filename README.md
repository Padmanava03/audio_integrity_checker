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
- **Integrity Reports:** Generates a **PDF report** of the integrity check.

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
### **Step 3: Set up MySQL Database**
Before running the application, set up the MySQL database:
```sh
python -c "import database; database.create_database()"
```
Modify database.py if you need to update MySQL credentials.
### **Step 4: Run the Application**
```sh
python gui.py
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
6. s**A PDF integrity report is generated**, detailing the verification results.
