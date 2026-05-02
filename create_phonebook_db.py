#Elliott Morris, 4/29/2026, create_phonebook_db.py

import sqlite3

def create_phonebook_db():
    try:
        # Connect to the database (creates it if it does not exist)
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()

        # Delete the old Entries table if it already exists
        cur.execute('DROP TABLE IF EXISTS Entries')

        cur.execute('''
            CREATE TABLE Entries (
                Name TEXT,
                PhoneNumber TEXT
            )''')

        conn.commit()
        print("Database 'phonebook.db' recreated successfully with a fresh 'Entries' table.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        conn.close()

# Run the function
if __name__ == '__main__':
    create_phonebook_db()
