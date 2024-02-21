import sqlite3
import os

from bot.misc import BD_PATH


def add_new_manga(title):
    conn = sqlite3.connect(BD_PATH)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO mangas (title) VALUES (?)", (title,))

    conn.commit()
