import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Adminuser",
    database = "hospetaldb"
)

mycursor = mydb.cursor()




