import os
import mysql.connector
import serial

serialConn = serial.Serial('COM12', 9600)


def create_database():
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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authorised_cards (
            entry INTEGER PRIMARY KEY AUTO_INCREMENT,
            card_id TEXT
        )
    ''')

    # Close the cursor and the connection
    cursor.close()
    connection.close()


def insert_card(card_id):
    print(card_id)
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
    cursor.execute("INSERT INTO authorised_cards(card_id) VALUES (%s)",(card_id,))

    # Commit the changes
    connection.commit()

    # Close the cursor and the connection
    cursor.close()
    connection.close()


def main():
    create_database()
    card_id = serialConn.readline().decode('utf-8')
    insert_card(card_id)


if __name__ == "__main__":
    main()