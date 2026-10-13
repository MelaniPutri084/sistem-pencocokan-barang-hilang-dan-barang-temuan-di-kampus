import mysql.connector
from mysql.connector import Error


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="db_temukan"
        )
        return connection

    except Error as e:
        print("Koneksi database gagal:", e)
        return None