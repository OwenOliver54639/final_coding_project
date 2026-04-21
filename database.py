import sqlite3
import bcrypt


def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_entries_db():
    conn = sqlite3.connect("entries.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    e_conn = get_entries_db()
    # Add your new table between lines 15 & 16.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.excute("""
      CREATE TABLE IF NOT EXISTS user(
      username TEXT PRIMARY KEY,
      password TEXT
      )
      """) 
    conn.commit()
    conn.close()