from mysql import *
import mysql.connector 


#conn = mysql.connector.connect(host = "localhost",username = 'root',password = 'Adminuser',database = 'hospetaldb')
#my_cursor = conn.cursor()

#val = (2,"Abdalaziz",22,"mail","Qena","0105286981","2020-01-01","DR",15,"B",15.2)
#my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",val)

#conn.commit()
#conn.close()


#sql = "insert into %s values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

#val = (table,Data[0],Data[1],Data[2],Data[3],Data[4],Data[5],Data[6],Data[7],Data[8],Data[9],Data[10])

Data = [3,"Abdalaziz",22,"mail","Qena","0105286981","2020-01-01","DR",15,"B",15.2]

table = 'employee'


def add(tuple,data):
    val = []
    for i in data:
        val.append(i)

    y = tuple(val)
    
f"isert into %s values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


    print(sql,table,y)
add('employee',Data)