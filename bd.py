import mysql.connector
from mysql.connector import errorcode

def conectarbanco():
  try:
    cnx = mysql.connector.connect(user='cshpco98_viquetti',
                                  database='cshpco98_estoque',
                                  password = 'Bananaverde333@',
                                  host = 'cshp.com.br')
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
      print(errorcode.ER_ACCESS_DENIED_ERROR)
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
