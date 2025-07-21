import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword"
)
mycursor = mydb.cursor()
mycursor.execute("select * from test2.student_detail")
for row in mycursor.fetchall():
    print(row)
mydb.close()