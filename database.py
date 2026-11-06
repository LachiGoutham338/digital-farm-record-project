import mysql.connector


def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MySQL password",          # Put your MySQL password here
        database="digital_farm"
    )

    return connection