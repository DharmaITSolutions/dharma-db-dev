import sqlite3
from db_connection import create_db_connection



print("enter customer name:")
customer_name = input()



def insert_customer(connection, customer_id, customer_name, customer_email, customer_phone, customer_address, customer_city, customer_state, customer_zip, customer_country):
    try:
        with connection:
            insert_sql = '''
            INSERT INTO customers (customer_id, customer_name, customer_email, customer_phone, customer_address, customer_city, customer_state, customer_zip, customer_country)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            connection.execute(insert_sql, (customer_id, customer_name, customer_email, customer_phone, customer_address, customer_city, customer_state, customer_zip, customer_country))
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

# Example usage
connection = create_db_connection()
if connection is not None:
    insert_customer(connection, 2, customer_name, 'example@email.com', '1234567890', '1234 Main St', 'Anytown', 'Anystate', '12345', 'USA')
    # Make sure to close the connection after all database operations are done
    connection.close()