import sqlite3
from db_connection import create_db_connection
from sqlite3_create_db import insert_customer, insert_product, insert_order, insert_order_item, insert_api_log

def input_customer_data():
    print("Enter customer details:")
    customer_id = input("Customer ID: ")
    customer_name = input("Name: ")
    customer_email = input("Email: ")
    customer_phone = input("Phone: ")
    customer_address = input("Address: ")
    customer_city = input("City: ")
    customer_state = input("State: ")
    customer_zip = input("ZIP: ")
    customer_country = input("Country: ")

    connection = create_db_connection()
    if connection:
        insert_customer( customer_id, customer_name, customer_email, customer_phone, customer_address, customer_city, customer_state, customer_zip, customer_country)
        connection.close()

def input_product_data():
    print("Enter product details:")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    currency = input("Currency: ")
    product_type = input("Product Type: ")

    connection = create_db_connection()
    if connection:
        insert_product(connection, product_name, price, currency, product_type)
        connection.close()

def input_order_data():
    print("Enter order details:")
    stripe_id = input("Stripe ID: ")
    printful_id = input("Printful ID: ")
    customer_id = input("Customer ID: ")
    order_date = input("Order Date (YYYY-MM-DD): ")
    delivery_date = input("Delivery Date (YYYY-MM-DD): ")
    shipping_address = input("Shipping Address: ")
    payment_status = input("Payment Status: ")
    status = input("Status: ")

    connection = create_db_connection()
    if connection:
        insert_order(connection, stripe_id, printful_id, customer_id, order_date, delivery_date, shipping_address, payment_status, status)
        connection.close()

def input_order_item_data():
    print("Enter order item details:")
    order_id = int(input("Order ID: "))
    product_id = int(input("Product ID: "))
    quantity = int(input("Quantity: "))

    connection = create_db_connection()
    if connection:
        insert_order_item(connection, order_id, product_id, quantity)
        connection.close()

def input_api_log_data():
    print("Enter API log details:")
    api_name = input("API Name: ")
    request_details = input("Request Details: ")
    response_details = input("Response Details: ")

    connection = create_db_connection()
    if connection:
        insert_api_log(connection, api_name, request_details, response_details)
        connection.close()

def main():
    while True:
        print("\nChoose an option to insert data:")
        print("1. Customer")
        print("2. Product")
        print("3. Order")
        print("4. Order Item")
        print("5. API Log")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            input_customer_data()
        elif choice == '2':
            input_product_data()
        elif choice == '3':
            input_order_data()
        elif choice == '4':
            input_order_item_data()
        elif choice == '5':
            input_api_log_data()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
