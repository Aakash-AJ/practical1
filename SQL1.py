import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

