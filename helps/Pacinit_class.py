import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Adminuser",
    database = "hospetaldb"
)

mycursor = mydb.cursor()




class Patient:
    # Adding method
    def adding(self,id, first_name, address, mobile_no,visit_date, waiting_time, Entry_time, Dr_name, chronic_diseases, Cost_visit):
        
        sql = "INSERT INTO Pacinits(id,first_name,address,mobile_no,visit_date,waiting_time,Entry_time,Dr_name,chronic_diseases,Cost_visit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (id,first_name, address, mobile_no,visit_date, waiting_time, Entry_time, Dr_name, chronic_diseases, Cost_visit)
        
        mycursor.execute(sql,val)

        mydb.commit()


    def update(self,id, first_name, address, mobile_no, visit_date, waiting_time, Entry_time, Dr_name, chronic_diseases, Cost_visit):
        
        sql = """
                UPDATE Pacinits SET first_name = %s, address = %s, mobile_no = %s, visit_date = %s, waiting_time = %s, Entry_time = %s, Dr_name = %s, chronic_diseases = %s, Cost_visit = %s WHERE id = %s
                """
        val = (first_name, address, mobile_no, visit_date, waiting_time, Entry_time, Dr_name, chronic_diseases, Cost_visit,id)        
        mycursor.execute(sql,val)
        mydb.commit()

    
    def Delete(self):
        sql = """
                    -- SET SQL_SAFE_UPDATES = 0;
                    DELETE FROM Doctors2 WHERE  first_name = 'Abdala';

                    -- SET SQL_SAFE_UPDATES = 1; 

            """
        #val = (Id)
        
        mycursor.execute(sql)

        mydb.commit()


    def get_info(self,Id):
        sql = f"SELECT * FROM Pacinits WHERE id = {Id}"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:

            print(x)


P1 = Patient()
#P1.adding(1,"Ahmed", "Qena", "01095286981", "2020-12-12", 15, "1:55","khaled", "dieabets", 55.22)
#P1.update(1,"Ahmed", "Qena", "01060665545", "2020-12-12", 15, "1:55","khaled", "dieabets", 55.22)
P1.get_info(1)