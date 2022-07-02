import mysql.connector
import tkinter.messagebox

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Adminuser",
    database = "hospetaldb"
)

mycursor = mydb.cursor()

class Employ:
    def adding(self,id, name, address, mobile, jop, date, Ex_years, manager, specialization, Degree, salary):
        sql = "INSERT INTO employees (id, name, address, mobile, jop, date, Ex_years, manager, specialization, Degree, salary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (id, name, address, mobile, jop, date, Ex_years, manager, specialization, Degree, salary)
    
        mycursor.execute(sql,val)

        mydb.commit()

    


    def update(self,id, name, address, mobile, jop, date, Ex_years, manager, specialization, Degree, salary):
        
        sql = """
                UPDATE employess SET name = %s, address = %s, mobile = %s, job = %s, date = %s, Ex_years = %s, manager = %s, specialization = %s, Degree = %s, salary = %s  WHERE id = %s
                """
        val = (name, address, mobile, jop, date, Ex_years, manager, specialization, Degree, salary,id)        
        mycursor.execute(sql,val)
        mydb.commit()

    
    def Delete(self):
        sql = """
                    -- SET SQL_SAFE_UPDATES = 0;
                    DELETE FROM Doctors2 WHERE  first_name = 'Abdala';

                    -- SET SQL_SAFE_UPDATES = 1; 

            """
        
        
        mycursor.execute(sql)

        mydb.commit()


    def get_info(self,id):
        sql = f"SELECT * FROM hospetal1 WHERE Id = {id}"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:

            return x

e = Employ()

#e1 = Employ()
#e1.adding("4", "Abdalaziz", "qena", "01095286981", "dr", "2020-01-11","15", "osama", "sE", "B", "1500")

y = e.get_info(2)

if y == None:
    print(("not exist"))

else:
    print(y)