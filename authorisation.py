import os
import serial
import time
import mysql.connector
from insertion import create_database
from insertion import serialConn
# Set up the serial communication with Arduino - adjust the serial port and the baud rates as needed
def search_database(card_id):
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'diamant2233!'
    db_name = 'RFID_cards'

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    # Create a cursor object
    cursor = connection.cursor()
    # Execute the SQL query
    cursor.execute("SELECT * FROM authorised_cards WHERE card_id=(%s)", (card_id,))

    # Fetch the result
    result = cursor.fetchone()


    return result is not None


def main():
    create_database()  # Create the database table if it doesn't exist

    # Continuously read the card id from the Arduino and check if it's authorised
    while True:
        if serialConn.in_waiting > 0:
            card_id = serialConn.readline().decode('utf-8') # read only the first line
            authorised = search_database(card_id)
            if authorised:
                serialConn.write(b'A')
                print("Authorised")
            else:
                serialConn.write(b'D')
                print("Not authorised")
            time.sleep(1)
        else:
            time.sleep(0.1) # Sleep for a short period to avoid excessive looping


if __name__ == "__main__":
    main()