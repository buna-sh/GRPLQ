import sqlite3

MODULE_NAME = "Database Module"
VERSION = "1.0.0"

print(f"Database Module: Version {VERSION}")

def init():
    try:
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect("db.db")
        cursor = conn.cursor()
        
        # Create a sample table (you can customize this schema as needed)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Commit changes and close the connection
        conn.commit()
        conn.close()
        
        print("Database Module: Initialization complete. Database and table created (if they didn't exist).")
    except sqlite3.Error as e:
        print(f"Database Module: An error occurred: {e}")

def test():
    try:
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect("db.db")
        cursor = conn.cursor()

        print("Database Module: Connection test approved.")
    except sqlite3.Error as e:
        print(f"Database Module: An error occurred: {e}")


if __name__ == "__main__":
    init()
    test()
