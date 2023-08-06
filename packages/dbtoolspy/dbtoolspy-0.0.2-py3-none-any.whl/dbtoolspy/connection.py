import os
from mysql.connector import connect, Error
from dotenv import load_dotenv


def get_connection():
    ''' Returns a MySQL connection object '''

    load_dotenv()

    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')

    connection = None

    try:
        connection = connect(
            host=host,
            user=user,
            password=password
        )
    except Error as e:
        connection = str(e)

    return connection
