# !pip install mysql-connector-python

import mysql.connector

con = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "programography")

# if con.is_connected():
#     print("mysl connected sucessfully")



cuser = con.cursor()


# fetch record:

# cuser.execute("select * from Sududents_Info")
# zx = cuser.fetchall()
# print(zx)




# Update record:

# cuser.execute("update Sududents_Info set Age = 30 where Stu_Name = 'hlo'")
# con.commit()





# delete record :

cuser.execute("delete from Sududents_Info where Age = 20")
con.commit()




# insert record :

# cuser.execute("insert into Sududents_Info values('moris', 22, '298349', 'moris@gmail.com')")
# cuser.execute("insert into Sududents_Info values('hlo', 19, '982163892', 'hlo@gmail.com')")
# cuser.execute("insert into Sududents_Info values('programo', 22, '92864893', 'programo@gmail.com')")
# con.commit()






