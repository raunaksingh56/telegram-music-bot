import sqlite3
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)
conn = sqlite3.connect("data/musicbot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    user_id INTEGER,
    song_title TEXT,
    timestamp TEXT
)
""")
conn.commit()

def add_song_to_history(user_id: int, song_title: str):
    cursor.execute("INSERT INTO history (user_id, song_title, timestamp) VALUES (?, ?, ?)",
                   (user_id, song_title, datetime.now().isoformat()))
    conn.commit()

def get_last_songs(user_id: int, limit=5):
    cursor.execute("SELECT song_title FROM history WHERE user_id = ? ORDER BY timestamp DESC LIMIT ?",
                   (user_id, limit))
    return [row[0] for row in cursor.fetchall()]
