# Builds a SQL Database with Python and SQLite3 for order and customer management

import sqlite3

DATABASE_PATH = 'dharmatest.db'

def create_table(create_table_sql):
    """
    Creates a table from the create_table_sql statement
    :param create_table_sql: a CREATE TABLE statement
    """
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            conn.execute(create_table_sql)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

#Creates Dummy Data for testing
def insert_dummy_customer():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT EXISTS(SELECT 1 FROM customers WHERE customer_email = 'johndoe@example.com')")
        if not cursor.fetchone()[0]:
            cursor.execute('''
            INSERT INTO customers (customer_id, customer_name, customer_email, customer_phone, customer_address, customer_city, customer_state, customer_zip, customer_country)
            VALUES ('1', 'John Doe', 'johndoe@example.com', '1234567890', '1234 Main St', 'Anytown', 'Anystate', '12345', 'USA')
            ''')

def insert_dummy_product():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT EXISTS(SELECT 1 FROM products WHERE product_name = 'Sample Product')")
        if not cursor.fetchone()[0]:
            cursor.execute('''
            INSERT INTO products (product_name, price, currency, product_type)
            VALUES ('Sample Product', 19.99, 'USD', 'Sample Type')
            ''')

def insert_dummy_order():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT EXISTS(SELECT 1 FROM orders WHERE stripe_id = 'stripe123' AND printful_id = 'printful123')")
        if not cursor.fetchone()[0]:
            cursor.execute('''
            INSERT INTO orders (stripe_id, printful_id, customer_id, order_date, delivery_date, shipping_address, payment_status, status)
            VALUES ('stripe123', 'printful123', '1', '2021-01-01', '2021-01-10', '1234 Main St, Anytown, Anystate, 12345', 'Paid', 'Pending')
            ''')

def insert_dummy_order_item():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT EXISTS(SELECT 1 FROM order_items WHERE order_id = 1 AND product_id = 1)")
        if not cursor.fetchone()[0]:
            cursor.execute('''
            INSERT INTO order_items (order_id, product_id, quantity)
            VALUES (1, 1, 2)
            ''')

def insert_dummy_api_log():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT EXISTS(SELECT 1 FROM api_logs WHERE api_name = 'Stripe API' AND request_details = 'Request details here')")
        if not cursor.fetchone()[0]:
            cursor.execute('''
            INSERT INTO api_logs (api_name, request_details, response_details)
            VALUES ('Stripe API', 'Request details here', 'Response details here')
            ''')


#Insert Functions: 
def insert_customer(customer_id, customer_name, customer_email, customer_phone, customer_address, customer_city, customer_state, customer_zip, customer_country):
    with sqlite3.connect(DATABASE_PATH) as conn:
        insert_sql = '''
        INSERT INTO customers (customer_id, customer_name, customer_email, customer_phone, customer_address, customer_city, customer_state, customer_zip, customer_country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        conn.execute(insert_sql, (customer_id, customer_name, customer_email, customer_phone, customer_address, customer_city, customer_state, customer_zip, customer_country))

def insert_product(product_name, price, currency, product_type):
    with sqlite3.connect(DATABASE_PATH) as conn:
        insert_sql = '''
        INSERT INTO products (product_name, price, currency, product_type)
        VALUES (?, ?, ?, ?)
        '''
        conn.execute(insert_sql, (product_name, price, currency, product_type))

def insert_order(stripe_id, printful_id, customer_id, order_date, delivery_date, shipping_address, payment_status, status):
    with sqlite3.connect(DATABASE_PATH) as conn:
        insert_sql = '''
        INSERT INTO orders (stripe_id, printful_id, customer_id, order_date, delivery_date, shipping_address, payment_status, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        conn.execute(insert_sql, (stripe_id, printful_id, customer_id, order_date, delivery_date, shipping_address, payment_status, status))

def insert_order_item(order_id, product_id, quantity):
    with sqlite3.connect(DATABASE_PATH) as conn:
        insert_sql = '''
        INSERT INTO order_items (order_id, product_id, quantity)
        VALUES (?, ?, ?)
        '''
        conn.execute(insert_sql, (order_id, product_id, quantity))

def insert_api_log(api_name, request_details, response_details):
    with sqlite3.connect(DATABASE_PATH) as conn:
        insert_sql = '''
        INSERT INTO api_logs (api_name, request_details, response_details)
        VALUES (?, ?, ?)
        '''
        conn.execute(insert_sql, (api_name, request_details, response_details))


def main():
    # Need to create promo codes table & associated rows & functions
    create_customers_table = ('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id TEXT PRIMARY KEY,
        customer_name TEXT NOT NULL,
        customer_email TEXT NOT NULL UNIQUE,
        customer_phone TEXT,
        customer_address TEXT,
        customer_city TEXT,
        customer_state TEXT,
        customer_zip TEXT,
        customer_country TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    create_products_table = ('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price DECIMAL NOT NULL,
        currency TEXT NOT NULL,
        product_type TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    create_orders_table = ('''
        CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        stripe_id TEXT NOT NULL,
        printful_id TEXT NOT NULL,
        customer_id TEXT NOT NULL,
        order_date DATE NOT NULL,
        delivery_date DATE,
        shipping_address TEXT,
        payment_status TEXT CHECK( payment_status IN ('Paid', 'Pending', 'Failed') ),
        status TEXT CHECK( status IN ('Pending', 'Completed', 'Cancelled') ) NOT NULL DEFAULT 'Pending',
        promo_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (promo_id) REFERENCES promo_codes(promo_id)
    )
    ''')

    create_order_items_table = ('''
    CREATE TABLE IF NOT EXISTS order_items (
        order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    ''')

    create_api_log_table = ('''
    CREATE TABLE IF NOT EXISTS api_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        api_name TEXT NOT NULL,
        request_details TEXT,
        response_details TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    create__promo_codes_table = ('''CREATE TABLE IF NOT EXISTS promo_codes (
    promo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    discount_value DECIMAL NOT NULL,
    valid_from DATE,
    valid_until DATE,
    active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    create_table(create_customers_table)
    create_table(create_products_table)
    create_table(create_orders_table)
    create_table(create_order_items_table)
    create_table(create_api_log_table)
    create_table(create__promo_codes_table)

    insert_dummy_customer()
    insert_dummy_product()
    insert_dummy_order()
    insert_dummy_order_item()
    insert_dummy_api_log()

    # Example usage of insert functions
    # insert_customer('1', 'John Doe', 'johndoe@example.com', '1234567890', '1234 Main St', 'Anytown', 'Anystate', '12345', 'USA')
    # insert_product('Sample Product', 19.99, 'USD')
    # insert_order('stripe123', 'printful123', '1', '2021-01-01', '2021-01-10', '1234 Main St, Anytown, Anystate, 12345', 'Paid', 'Pending')
    # insert_order_item(1, 1, 2)
    # insert_api_log('Stripe API', 'Request details here', 'Response details here')


if __name__ == '__main__':
    main()
