# !pip install mysql-connector-python

import mysql.connector

con = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "programography")

# if con.is_connected():
#     print("mysl connected sucessfully")



cuser = con.cursor()

cuser.execute("")
