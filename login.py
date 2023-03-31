import pymysql as pms
conn = pms.connect(host="localhost", 
                   port=3306,
                   user="root",
                   password="Harini07#",
                   db="harini")
print(conn)
cursor=conn.cursor()

def getcredentials():
    username =[]
    pwd=[]
    cursor.execute("SELECT * FROM harinilogin ")
    result =cursor.fetchall()
    print(result)
    for i in result:
        username.append(i[0])
        pwd.append(i[1])
    return username , pwd