import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.student_detail values ('Aakash', 'AJ', 23, 'AJ9833@gmail.com')")
mydb.commit()
mydb.close()