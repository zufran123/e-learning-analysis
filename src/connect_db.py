import sqlite3

def create_connection(db_path="data/elearning_platform.db"):
    try:
        conn = sqlite3.connect(db_path)
        print("✅ Connected to database")
        return conn
    except sqlite3.Error as e:
        print("❌ Database connection failed:", e)
        return None