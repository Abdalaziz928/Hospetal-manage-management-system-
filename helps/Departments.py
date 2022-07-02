import mysql.connector


class Person:
    def __init__(self,Id,name,age,address,mobile,date):
        self.Id = Id
        self.name = name
        self.age = age
        self.address = address
        self.mobile = mobile
        self.date = date

    

    def Exit(root):
        exitbtn =messagebox.askyesno("Are you sure you want to exit?")
        if exitbtn > 0:
                root.destroy()


    def get_info(ID,table):
            conn = mysql.connector.connect(host = "localhost",username= "root",password = "Adminuser",database = "hospetaldb")
            my_cursor = conn.cursor()
            sql = f"SELECT * FROM {table} WHERE Id = {ID}"
            my_cursor.execute(sql)
            myresult = my_cursor.fetchall()
            for x in myresult:

                return x

            conn.commit()
            conn.close()


    def Evalution(ID):
            y = get_info(ID)

            if(y == None):
                return True
            else:
                return False


    def update(Id,list1):
            d= str(Id.get())

            if (d == ""):

                messagebox.showerror("Error","Pleas Enter ID")

            else:


                if(d.isnumeric()):
                    d1 = int(d)
                    if(not (Evalution(d1))):
                    
                        
                        x = get_info(d1)
                        #list1 = [name(),age(),Gander(),address(),mobile(),date(),deses(),Blood(),Clinec(),Room(),Companion()]
                        list2 = []
                        for i in range(len(list1)):
                            if list1[i] == '':
                                list2.append(x[i+1])

                            else: 
                                list2.append(list1[i])


                        conn = mysql.connector.connect(host = "localhost",username= "root",password = "Adminuser",database = "hospetaldb")
                        mycursor = conn.cursor()

                        if len(list1) == 11:

                            sql = """
                            UPDATE hospetal1 SET name = %s, age = %s, gander = %s, address = %s, mobile = %s, date = %s, deses = %s, blood = %s, clinec = %s, room = %s,companion = %s  WHERE Id = %s
                                """
                            val = (list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],list2[8],list2[9],list2[10],d1)   
                        else:
                            sql = """
                            UPDATE hospetal1 SET name = %s, age = %s, gander = %s, address = %s, mobile = %s, date = %s, deses = %s, blood = %s, clinec = %s, room = %s,companion = %s  WHERE Id = %s
                                """
                            val = (list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],list2[8],list2[9],list2[10],list1[11],d1)   

                        mycursor.execute(sql,val)
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("success","data has been update")


                    else:
                        messagebox.showerror("Error", "This Id is not exist")

                else:
                    messagebox.showerror("Erro","This id is not valid")


