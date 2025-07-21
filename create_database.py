import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

