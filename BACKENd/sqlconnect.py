import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  # print("Opening mysql connection")
  global __cnx
  if __cnx is None:
      __cnx = mysql.connector.connect(user='root', password='Kanakam@1234', host='127.0.0.1', database='zomato_db')
  return __cnx
