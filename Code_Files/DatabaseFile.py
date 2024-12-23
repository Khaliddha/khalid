import sqlite3

# Database file name
DB_FILE = 'weather_data.db'

# Create the database and table if they don't exist
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL,
            humidity INTEGER,
            description TEXT
        )
    ''')
    conn.commit()

print(f"Database '{DB_FILE}' initialized successfully.")

