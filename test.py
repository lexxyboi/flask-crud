import mysql.connector

try:
    connection = mysql.connector.connect(
        user='root',
        password='1234',
        host='localhost',
        database='person'
    )
    print("Successfully connected to the database.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection:
        connection.close()
