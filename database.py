import sqlite3

DB_PATH = "audio_hashes.db"

def init_db():
    """Initialize the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hashes (
            file_path TEXT PRIMARY KEY,
            hash_value TEXT
        )
    """)
    conn.commit()
    conn.close()

def store_hash(file_path, hash_value):
    """Store hash of an audio file"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO hashes (file_path, hash_value) VALUES (?, ?)", (file_path, hash_value))
    conn.commit()
    conn.close()

def check_hash(hash_value):
    """Check if hash exists in the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM hashes WHERE hash_value = ?", (hash_value,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Initialize database on module import
init_db()
