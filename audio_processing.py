import hashlib
import librosa
import numpy as np
from database import store_hash, check_hash

def generate_hash(audio_path):
    """Generate SHA256 hash for an audio file"""
    with open(audio_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

def process_audio(audio_path):
    """Process audio file and store hash in the database"""
    file_hash = generate_hash(audio_path)
    store_hash(audio_path, file_hash)
    print(f"Hash stored for {audio_path}: {file_hash}")

def verify_audio(audio_path):
    """Verify audio integrity by comparing stored hash"""
    file_hash = generate_hash(audio_path)
    return check_hash(file_hash)
