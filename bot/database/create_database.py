import sqlite3
import os

from bot.misc import BD_PATH


def create_database():
    conn = sqlite3.connect(BD_PATH)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS mangas(
        id INT PRIMARY KEY,
        title TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS chapters(
        id INT,
        chapter_number INT,
        telegraph_url TEXT,
        google_disk_url TEXT
    )''')

    conn.commit()
