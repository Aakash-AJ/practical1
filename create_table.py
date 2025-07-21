import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword"
)
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS test2.student_detail ("
    "first_name VARCHAR(50) NOT NULL, "
    "last_name VARCHAR(50) NOT NULL, "
    "age INT, "
    "email VARCHAR(100) UNIQUE)"
)
mydb.close()