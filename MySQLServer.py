# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",     
        password="2025",
        use_pure=True
    )

    cursor = connection.cursor()

    # Create database using IF NOT EXISTS to prevent error if it already exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Clean up: close cursor and connection if open
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
