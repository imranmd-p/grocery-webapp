import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx

<<<<<<< Updated upstream
    if __cnx is None:
        __cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Allsmall@123",
            database="grocery_db"
        )

    return __cnx
=======
  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='Allsmall@123', database='grocery_db')
>>>>>>> Stashed changes


