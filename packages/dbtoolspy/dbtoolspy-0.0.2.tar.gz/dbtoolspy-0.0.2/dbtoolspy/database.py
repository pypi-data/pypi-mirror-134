import os
from mysql.connector import connect
from dotenv import load_dotenv
from connection import get_connection


def get_db(db_name=None):
    ''' Returns a connection to the database '''

    load_dotenv()
    connection = get_connection()

    if db_name is None:
        db_name = os.getenv('DB_NAME')

        # check if database already exists if not create it
        cursor = connection.cursor()
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {db_name}".format(db_name=db_name))

        # commit/save changes to connection
        connection.commit()

        # set the database name
        connection.database = db_name
    else:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {db_name}".format(db_name=db_name))

        # commit/save changes to connection
        connection.commit()

        # set the database
        connection.database = db_name

        # set the environment variable to the custom database name
        os.environ['DB_NAME'] = db_name

    db = connection
    return db
