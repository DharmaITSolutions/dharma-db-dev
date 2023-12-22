import sqlite3

DATABASE_PATH = 'dharmatest.db'

def create_db_connection():
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        print("Successfully connected to the database.")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# # Example usage
# conn = create_db_connection()
# if conn is not None:
#     # Perform database operations
#     # ...

#     conn.close()
