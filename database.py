import sqlite3
import bcrypt


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

<<<<<<< HEAD
def init_db():
    try:
        conn = get_db()
        # Add your new table between lines 15 & 16.
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)
        conn.excute("""
            CREATE TABLE IF NOT EXISTS works(
            title TEXT PRIMARY KEY,
            author TEXT,
            image TEXT,
            )
        """) 
            
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    
    finally:
        conn.close()

    print("\nDatabase seeding complete!")
        
=======
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
>>>>>>> 1fe1245 (remove secret)
