import mysql.connector


#mycursor.execute("CREATE DATABASE harini")
#mycursor.execute("CREATE TABLE harinilogin (email VARCHAR(255), password  VARCHAR(255))")

'''def sqlsignup(emal,pwd):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Harini07#",
      database="harini"
    )

    mycursor = mydb.cursor()

    print(emal,pwd)
    sql = "INSERT INTO harinilogin (email,password) VALUES (%s, %s)"
    val = (emal,pwd)
    mycursor.execute(sql, val)
    mydb.commit()
'''

def sqllogin(email,password):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Harini07#",
      database="harini"
    )

    mycursor = mydb.cursor()

    query = f"SELECT password FROM harinilogin WHERE email='{email}'"
    mycursor.execute(query)
    pas=mycursor.fetchone()
    if not pas:
        return "nouser"
    elif pas[0]==password:
        return "found"
    else:
         return "wrongpass"